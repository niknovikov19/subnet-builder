import json
from pathlib import Path
import pickle as pkl
import sys

import numpy as np

sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
import common as cmn
from subnet_par_builder import SubnetParamBuilder, SubnetDesc


dirpath_work = Path(r'D:\WORK\Salvador\repo\subnet_tuner\test\model_PD2_L24_Izh2')

fpath_par_orig = dirpath_work / 'model.json'
with open(fpath_par_orig, 'r') as fid:
    par = json.load(fid)
    
tlim = (0, None)
sim_name = 'sim_res'
postfix = f'(t={tlim[0]}-{tlim[1]})'
fpath_rates = dirpath_work / f'{sim_name}_pop_rates_{postfix}.pkl'
fpath_spikes = dirpath_work / f'{sim_name}_spikes_{postfix}.pkl'
    
# Load firing rates
with open(fpath_rates, 'rb') as fid:
    pop_rate_data = pkl.load(fid)
# Load spikes
with open(fpath_spikes, 'rb') as fid:
    spikes = pkl.load(fid)
    
#inp_type = 'poiss'
inp_type = 'replay'
#inp_type = 'replay_jit'

freeze_conn = 0

# Subnet description
desc = SubnetDesc()
desc.pops_active = ['L2e', 'L2i', 'poissL2e', 'poissL2i']
if freeze_conn:
    desc.conns_frozen = ['L2e->L2e', 'L2e->L2i', 'L2i->L2e', 'L2i->L2i']
else:
    desc.conns_frozen = []
for pop in pop_rate_data:
    if pop not in desc.pops_active:
        if inp_type == 'poiss':
            desc.inp_surrogates[pop] = {
                'type': 'irregular',
                'rate': np.mean(pop_rate_data[pop]),
                'noise': 1.0
                }
        elif inp_type == 'replay':
            desc.inp_surrogates[pop] = {
                'type': 'spike_replay',
                'spkTimes': spikes[pop]
                }
        elif inp_type == 'replay_jit':
            desc.inp_surrogates[pop] = {
                'type': 'spike_replay_jit',
                'spkTimes': spikes[pop]
                }

spb = SubnetParamBuilder()
par_sub = spb.build(par, desc)

fpath_par_sub = dirpath_work / f'model_sub_(inp={inp_type}_frzconn={freeze_conn}).json'
with open(fpath_par_sub, 'w') as fid:
    json.dump(par_sub, fid, cls=cmn.NumpyEncoder, indent=4)
