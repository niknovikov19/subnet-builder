import json
from pathlib import Path
import pickle as pkl

from netpyne import sim
import numpy as np
from matplotlib import pyplot as plt

#import common as smn
import sim_res_parse_utils as srp


fpath_sim_res = (r'D:\WORK\Salvador\repo\A1_model_old\data\A1_paper'
                 r'\v34_batch56_10s_data.pkl')
fpath_out = (r'D:\WORK\Salvador\repo\A1_model_old\data\A1_paper'
                 r'\v34_batch56_10s_pop_rates.pkl')

with open(fpath_sim_res, 'rb') as fid:
    sim_res = pkl.load(fid)
    
pop_names = srp.get_pop_names(sim_res)
pop_rate_data = {}
for pop_name in pop_names:
    pop_rate_data[pop_name] = srp.get_pop_cell_rates(sim_res, pop_name)

with open(fpath_out, 'wb') as fid:
    pkl.dump(pop_rate_data, fid)
    
# =============================================================================
# rr = {pop_name: np.nanmax(r) for pop_name, r in pop_rate_data.items()}
# 
# S = srp.get_pop_spikes(sim_res, 'CT6', combine_cells=False)
# plt.figure()
# for n, s in enumerate(S):
#     plt.plot(s, [n] * len(s), 'k.')
# =============================================================================
