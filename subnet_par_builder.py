import copy
from dataclasses import dataclass, field

import numpy as np


def deepcopy2(x):
    if isinstance(x, dict):
        return {key: deepcopy2(val) for key, val in x.items()}
    elif isinstance(x, list):
        return [deepcopy2(val) for val in x]
    elif hasattr(x, '__dict__'):
        y = copy.copy(x)
        for attr_name in x.__dict__:
            attr_val = getattr(x, attr_name)
            attr_val = deepcopy2(attr_val)
            setattr(y, attr_name, attr_val)
        return y
    else:
        return x

def to_list(x):
    return np.atleast_1d(x).tolist()

def lists_intersect(list1, list2):
    return bool(set(list1) & set(list2))


@dataclass
class SubnetDesc:
    """
    Description of a sub-network model.

    Attributes:
        pops_active (list): names of pops that remain unchanged ("active")
        conns_frozen (list): names of conns between active pops that are frozen
        inp_surrogates (dict): params of spike generators that serve as
            surrogate replacements of frozen populations
    """    
    pops_active: list = field(default_factory=list)
    conns_frozen: list = field(default_factory=list)
    inp_surrogates: dict = field(default_factory=dict)
    
    def save(self, fpath): pass
    def load(self, fpath): pass
    

class SubnetParamBuilder:
    """
    Class for converting a full network model into a sub-network model,
    where some of the populations are "frozen" - i.e. replaced by equivalent
    surrogate spike generators
    
    Attributes:
        
    """
    def __init__(self):
        self.pops_active = []
        self.pops_frozen = []
        self.subnet_desc = None
        self.netpar_full = {}
        self.netpar_sub = {}
        
    def build(self, netpar_full, subnet_desc):
        self.netpar_full = netpar_full
        self.subnet_desc = subnet_desc
        self._init_netpar_sub()
        self._find_active_pops()
        self._find_frozen_pops()
        self._copy_active_pops()
        self._copy_conns()
        self._create_frozen_pops()
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
        return list(self.netpar_full['popParams'].keys())
    
    def _get_all_conns(self, par_group='connParams'):
        """Get all (sub-)connections of the full model. """
        if par_group in self.netpar_full:
            return list(self.netpar_full[par_group].keys())
        else:
            return []
    
    #def _get_active_pops(self):
    #    return self.subnet_desc.pops_active
    
    def _get_2pop_conns(self, pops_pre, pops_post):
        """Find connections between two sets of pops in the full model. """
        conns = []
        for conn in self.netpar_full['connParams']:
            pops_pre_ = self._get_conn_pops_presyn(conn)
            pops_post_ = self._get_conn_pops_postsyn(conn)
            if (lists_intersect(pops_pre, pops_pre_) and
                lists_intersect(pops_post, pops_post_)):
                conns.append(conn)
        return conns
            
    def _is_active_input(self, pop_pre):
        """Check if pop_pre has non-frozen projections to active populations. """
        for pop_post in self.subnet_desc.pops_active:
            conns = self._find_2pop_conns(pop_pre, pop_post)
            for conn in conns:
                if conn not in self.subnet_desc.conns_frozen:
                    return True
        return False
    
    def _find_active_pops(self):
        self.pops_active = self.subnet_desc.pops_active.copy()
        
    def _find_frozen_pops(self):
        self.pops_frozen = []
        for pop_pre in self._get_all_pops():
            # Connections from pop_pre to active populations
            conns = self._get_2pop_conns(
                [pop_pre], self.subnet_desc.pops_active)
            if len(conns) != 0:
                # Non-active pop. projecting to an active pop.
                if pop_pre not in self.subnet_desc.pops_active:
                    self.pops_frozen.append(pop_pre)
                else:
                    # Active pop. with a frozen projection to an active pop.
                    if any([conn in self.subnet_desc.conns_frozen
                            for conn in conns]):
                        self.pops_frozen.append(pop_pre)
        self.pops_frozen = list(set(self.pops_frozen))  # unique entries
    
    def _copy_active_pops(self):
        for pop in self.pops_active:
            self.netpar_sub['popParams'][pop] = (
                deepcopy2(self.netpar_full['popParams'][pop]))
    
    def _get_cond_pops(self, conds):
        """Return a list of populations that meet the conditions conds. """
        # Note: could return a superset of the actual list
        if 'pop' in conds:
            return to_list(conds['pop'])
        elif 'cellType' in conds:
            pops = []
            for pop, par in self.netpar_full['popParams'].items():
                if 'cellType' in par:
                    if par['cellType'] in to_list(conds['cellType']):
                        pops.append(pop)
            return pops
        else:
            raise ValueError('Conditions should contain "pop" or "cellType"')
    
    def _get_conn_pops_presyn(self, conn, par_group='connParams'):
        """Get pre-synaptic populations of a (sub-)connection (from full model). """
        conds = self.netpar_full[par_group][conn]['preConds']
        return self._get_cond_pops(conds)
            
    def _get_conn_pops_postsyn(self, conn, par_group='connParams'):
        """"Get post-synaptic populations of a (sub-)connection (from full model). """
        conds = self.netpar_full[par_group][conn]['postConds']
        return self._get_cond_pops(conds)
    
    def _rename_conn_pop_presyn(self, conn, pop_old, pop_new, par_group='connParams'):
        """Rename pre-synaptic population of a (sub-)connection (in subnet model). """
        conds = self.netpar_sub[par_group][conn]['preConds']
        if 'pop' in conds:
            pops = to_list(conds['pop'])
            pops = [pop_new if pop == pop_old else pop for pop in pops]
            if len(pops) == 1:
                pops = pops[0]
            conds['pop'] = pops
            
    def _remove_inact_conn_pops_postsyn(self, conn, par_group='connParams'):
        conds = self.netpar_sub[par_group][conn]['postConds']
        if 'pop' in conds:
            pops = to_list(conds['pop'])
            pops = [pop for pop in pops if pop in self.pops_active]
            if len(pops) == 1:
                pops = pops[0]
            conds['pop'] = pops
    
    def _gen_frozen_pop_name(self, pop):
        return pop + 'frz'
    
    def _copy_conns(self):
        """Copy relevant (sub-)connections from full to subnet model params. """
        for par_group in ('connParams', 'subCnnParams'):
            for conn in self._get_all_conns(par_group):
                pops_pre = self._get_conn_pops_presyn(conn, par_group)
                pops_post = self._get_conn_pops_postsyn(conn, par_group)
                # Skip (sub-)connections with nonactive target pops.
                if not lists_intersect(pops_post, self.pops_active):
                    continue
                # Copy (sub-)connection params from full to subnet model
                self.netpar_sub[par_group][conn] = (
                    deepcopy2(self.netpar_full[par_group][conn]))
                # If a pre-synaptic pop or the conn itself is frozen,
                # then change the name of the pre-synaptic pop to a surrogate
                for pop_pre in pops_pre:
                    need_rename = False
                    if pop_pre not in self.pops_active:
                        need_rename = True
                    if ((par_group == 'connParams') and                         
                        (conn in self.subnet_desc.conns_frozen)):
                        need_rename = True
                    if need_rename:
                        pop_pre_frozen = self._gen_frozen_pop_name(pop_pre)
                        self._rename_conn_pop_presyn(
                            conn, pop_pre, pop_pre_frozen, par_group)
                # Remove inactive post-synaptic populations for the conn
                self._remove_inact_conn_pops_postsyn(conn, par_group)
    
    def _create_frozen_pops(self):
        for pop in self.pops_frozen:
            self._create_frozen_pop(pop)
                
    def _create_frozen_pop(self, pop):
        inp_desc = self.subnet_desc.inp_surrogates[pop]
        # Pop. params common for all type of surrogate input
        par0 = self._make_inp_params_common(pop)
        # Pop. params specific for each surrogate input type
        if inp_desc['type'] == 'irregular':
            par = self._make_inp_params_irregular(pop)
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
            'yRange', 'ynormRange', 'zRange', 'znormRange', 'cellType'
            ]
        par = {key: deepcopy2(val) for key, val in par_orig.items()
               if key in keys_tocopy}
        return par
    
    def _make_inp_params_irregular(self, pop):
        """Pop. params specific for each surrogate input type. """
        inp_desc = self.subnet_desc.inp_surrogates[pop]
        keys_tocopy = ['interval', 'rate', 'noise', 'inp_desc', 'number', 'seed']
        par = {key: deepcopy2(val) for key, val in inp_desc.items()
               if key in keys_tocopy}
        par['cellModel'] = 'NetStim'
        return par
                
        
        
        
        