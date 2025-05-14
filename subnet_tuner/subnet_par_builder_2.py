import copy
from dataclasses import dataclass, field
from typing import Dict, List, Literal

import numpy as np

from .netpar_utils import get_cond_pops, get_conn_pops_presyn, get_conn_pops_postsyn
from .subnet_desc import SubnetDesc
from .utils import deepcopy2, lists_intersect, to_list
    

class SubnetParamBuilder2:
    """
    Class for converting a full network model into a sub-network model,
    where some of the populations are "frozen" - i.e. replaced by equivalent
    surrogate spike generators
    
    Attributes:
        
    """
    def __init__(self):
        self.pops_active: List = []
        self.pops_frozen: List = []
        self.subnet_desc: SubnetDesc = None
        self.netpar_full: Dict = {}
        self.netpar_sub: Dict = {}
        
    def build(self, netpar_full, subnet_desc):
        self.netpar_full = netpar_full
        self.subnet_desc = subnet_desc
        self._init_netpar_sub()   # copy to subnet the params that won't be changed
        if self.subnet_desc.pops_active == 'all':
            self.pops_active = self._get_all_pops()
        else:
            self.pops_active = self.subnet_desc.pops_active.copy()
        self._copy_conns()   # self.pops_frozen will be also filled here
        self._copy_active_pops()
        self._create_frozen_pops()
        self._copy_stim_params()
        # TODO: subconn
        return self.netpar_sub
        
    def _init_netpar_sub(self):
        """Init to-be-modified params with {}, copy others from the full model. """
        self.netpar_sub = {}
        keys_upd = ['popParams', 'connParams', 'subConnParams', 'stimTargetParams']
        for key, val in self.netpar_full.items():
            if key in keys_upd:
                self.netpar_sub[key] = {}
            else:
                self.netpar_sub[key] = deepcopy2(val)
    
    def _get_all_pops(self):
        """Get all populations of the full model. """
        return list(self.netpar_full['popParams'].keys())
    
    def _get_all_conns(self, par_group='connParams'):
        """Get all (sub-)connections of the full model. """
        if par_group in self.netpar_full:
            return list(self.netpar_full[par_group].keys())
        else:
            return []
    
    def _get_all_stims(self):
        """Get all stim. targets of the full model. """
        if 'stimTargetParams' in self.netpar_full:
            return list(self.netpar_full['stimTargetParams'].keys())
        else:
            return []
    
    def _get_conn_par(self, conn, par_group='connParams'):
        return self.netpar_full[par_group][conn]
    
    def _is_pop_active(self, pop):
        return pop in self.pops_active

    def _is_conn_active(self, conn):
        if self.subnet_desc.conns_frozen == 'all':
            return False
        return not conn in self.subnet_desc.conns_frozen

    def _copy_conns(self):
        self.pops_frozen = []

        for conn in self._get_all_conns():
            pops_pre = self._get_conn_pops_presyn(conn)
            pops_post = self._get_conn_pops_postsyn(conn)

            # Leave active post-synaptic pops. only
            pops_post_new = [pop for pop in pops_post
                             if self._is_pop_active(pop)]
            if len(pops_post_new) == 0:
                continue   # all targets inactive - skip this connection
            conn_par_new = deepcopy2(self._get_conn_par(conn))   # a copy that will be added to the subnet
            conn_par_new['postConds']['pop'] = pops_post_new   # explicitly define postConds by pop list
            conn_par_new['postConds'].pop('cellType', None)   # if postConds were defined by cellType - clean it

            # Pre-synaptic pops. - original or frozen
            pops_pre_new = []
            for pop in pops_pre:
                if self._is_conn_active(conn) and self._is_pop_active(pop):
                    pops_pre_new.append(pop)   # active presynaptic pop.
                else:
                    pop_frz = self._gen_frozen_pop_name(pop)
                    pops_pre_new.append(pop_frz)
                    self.pops_frozen.append(pop)
            conn_par_new['preConds']['pop'] = pops_pre_new
            conn_par_new['preConds'].pop('cellType', None)   # if preConds were defined by cellType - clean it

            # Add the connection to the subnet
            self.netpar_sub['connParams'][conn] = conn_par_new
        
        self.pops_frozen = list(set(self.pops_frozen))   # remove duplicates
    
    def _copy_active_pops(self):
        print('Copy active pops...')
        for pop in self.pops_active:
            self.netpar_sub['popParams'][pop] = (
                deepcopy2(self.netpar_full['popParams'][pop]))
    
    def _get_cond_pops(self, conds):
        """Return a list of populations that meet the conditions conds. """
        return get_cond_pops(self.netpar_full, conds)
    
    def _get_conn_pops_presyn(self, conn, par_group='connParams'):
        """Get pre-synaptic populations of a (sub-)connection (from full model). """
        return get_conn_pops_presyn(self.netpar_full, conn, par_group)
            
    def _get_conn_pops_postsyn(self, conn, par_group='connParams'):
        """Get post-synaptic populations of a (sub-)connection (from full model). """
        return get_conn_pops_postsyn(self.netpar_full, conn, par_group)
    
    def _get_stim_pops_postsyn(self, stim):
        """"Get post-synaptic populations from stimTargetParams. """
        conds = self.netpar_full['stimTargetParams'][stim]['conds']
        return self._get_cond_pops(conds)

    def _gen_frozen_pop_name(self, pop):
        return pop + 'frz'
                    
    def _copy_stim_params(self):
        """Copy relevant entries of stimTargetParams. """
        print('Copy stim. targets...')
        for stim in self._get_all_stims():
            pops_post = self._get_stim_pops_postsyn(stim)
            # At least one of the stim. targets is active - copy the stim.
            if lists_intersect(pops_post, self.pops_active):
                self.netpar_sub['stimTargetParams'][stim] = (
                    deepcopy2(self.netpar_full['stimTargetParams'][stim]))
    
    def _create_frozen_pops(self):
        for pop in self.pops_frozen:
            self._create_frozen_pop(pop)
    
    def _create_frozen_pop(self, pop):
        inp_desc = self.subnet_desc.inp_surrogates[pop]
        # Pop. params common for all types of surrogate input
        par0 = self._make_inp_params_common(pop)
        # Pop. params specific for each surrogate input type
        if inp_desc['type'] == 'irregular':
            par = self._make_inp_params_irregular(pop)
        elif inp_desc['type'] in ('spike_replay', 'spike_replay_jit'):
            par = self._make_inp_params_replay(pop)
        else:
            raise ValueError('Invalid type of surrogate input')
        # Add frozen pop to sub-network
        pop_frozen =  self._gen_frozen_pop_name(pop)
        self.netpar_sub['popParams'][pop_frozen] = par0 | par
    
    def _make_inp_params_common(self, pop):
        """Pop. params common for all type of surrogate input. """
        par_orig = self.netpar_full['popParams'][pop]
        keys_tocopy = [
            'numCells', 'density', 'gridSpacing', 'xRange', 'xnormRange',
            'yRange', 'ynormRange', 'zRange', 'znormRange',
            #'cellType'
            ]
        par = {key: deepcopy2(val) for key, val in par_orig.items()
               if key in keys_tocopy}
        return par
    
    def _make_inp_params_irregular(self, pop):
        """Pop. params specific for each surrogate input type. """
        inp_desc = self.subnet_desc.inp_surrogates[pop]
        keys_tocopy = ['interval', 'rate', 'noise', 'number', 'seed']
        par = {key: deepcopy2(val) for key, val in inp_desc.items()
               if key in keys_tocopy}
        if 'noise' not in par:
            par['noise'] = 1.0
        par['cellModel'] = 'NetStim'
        return par
    
    '''def _jitter_spiketrains(self, spikes):
        """Apply a random circular time shift to each spiketrain. """
        spikes = [np.array(s) for s in spikes]
        T = np.max(np.concatenate(spikes))
        d = np.random.uniform(0, T, len(spikes))
        for n, s in enumerate(spikes):
            spikes[n] = np.sort((s + d[n]) % T)
        spikes = [list(s) for s in spikes]
        return spikes
    
    def _make_inp_params_replay(self, pop):
        """Pop. params specific for each surrogate input type. """
        inp_desc = self.subnet_desc.inp_surrogates[pop]
        keys_tocopy = ['spkTimes', 'number', 'seed']
        par = {key: deepcopy2(val) for key, val in inp_desc.items()
               if key in keys_tocopy}
        par['cellModel'] = 'VecStim'
        # Random circular shift of each spike train 
        if inp_desc['type'] == 'spike_replay_jit':
            par['spkTimes'] = self._jitter_spiketrains(par['spkTimes'])
        return par'''
        