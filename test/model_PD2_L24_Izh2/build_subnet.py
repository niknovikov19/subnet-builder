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
    
# Load firing rates
fpath_rates = dirpath_work / 'sim_res_pop_rates.pkl'
with open(fpath_rates, 'rb') as fid:
    pop_rate_data = pkl.load(fid)

# Subnet description
desc = SubnetDesc()
desc.pops_active = ['L2e', 'L2i', 'poissL2e', 'poissL2i']
desc.conns_frozen = []
for pop in pop_rate_data:
    if pop not in desc.pops_active:
        desc.inp_surrogates[pop] = {
            'type': 'irregular',
            'rate': np.mean(pop_rate_data[pop]),
            'noise': 1.0
            }

spb = SubnetParamBuilder()
par_sub = spb.build(par, desc)

fpath_par_sub = dirpath_work / 'model_sub.json'
with open(fpath_par_sub, 'w') as fid:
    json.dump(par_sub, fid, cls=cmn.NumpyEncoder, indent=4)