import json
from pathlib import Path
import pickle as pkl

from netpyne import sim
import numpy as np
from matplotlib import pyplot as plt

#import common as smn
import sim_res_parse_utils as srp


tlim = (1, 4)
dirpath_root = Path(r'D:\WORK\Salvador\repo\A1_model_old\data\A1_paper')
sim_name = 'v34_batch56_10s'

#tlim = (0, None)
#dirpath_root = Path(r'D:\WORK\Salvador\repo\subnet_tuner\test\model_PD2_L24_Izh2')
#sim_name = 'sim_res'


fpath_sim_res = dirpath_root / (sim_name + '_data.pkl')
postfix = f'(t={tlim[0]}-{tlim[1]})'
fpath_rates = dirpath_root / f'{sim_name}_pop_rates_{postfix}.pkl'
fpath_spikes = dirpath_root / f'{sim_name}_spikes_{postfix}.pkl'

# Load sim result
with open(fpath_sim_res, 'rb') as fid:
    sim_res = pkl.load(fid)

pop_names = srp.get_pop_names(sim_res)

# Get and save firing rates    
pop_rate_data = {}
for pop_name in pop_names:
    pop_rate_data[pop_name] = srp.get_pop_cell_rates(
        sim_res, pop_name, t0=tlim[0], tmax=tlim[1])
with open(fpath_rates, 'wb') as fid:
    pkl.dump(pop_rate_data, fid)
    
# Get and save spikes
spikes = {}
for pop_name in pop_names:
    spikes[pop_name] = srp.get_pop_spikes(
        sim_res, pop_name, t0=tlim[0], tmax=tlim[1], combine_cells=False,
        ms=True, ndigits=2)
with open(fpath_spikes, 'wb') as fid:
    pkl.dump(spikes, fid)
