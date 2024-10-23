# Compare firing rate distributions between several models

import os
from pathlib import Path
import pickle as pkl

import matplotlib.pyplot as plt
import numpy as np 

import sim_res_parse_utils as srp


#dirpath_data_root = Path(r'D:\WORK\Salvador\repo\A1_model_old\data')
dirpath_data_root = Path(r'D:\WORK\Salvador\repo\subnet_tuner\test\model_PD2_L24_Izh2')

# =============================================================================
# models_info = {
#     'full': {'path': ('A1_paper', 'v34_batch56_3s')},
#     'L3_subnet': {'path': ('exp_subnet_L3_3s', 'exp_subnet_L3_3s')}
#     }
# =============================================================================
models_info = {
    'full': {'path': 'sim_res'},
    'L2_subnet': {'path': 'sim_res_sub'}
    }

recalc_rates = False

#bins = 10
bins = np.linspace(0, 20, 10)


def _gen_model_path(model_name, postfix):
    info = models_info[model_name]
    if isinstance(info['path'], str):
        fpath = dirpath_data_root / (info['path'] + postfix)
    else:
        fpath = dirpath_data_root / info['path'][0] / (info['path'][1] + postfix)
    return str(fpath)

def _extract_rate_data(model_name, postfix_sim, postfix_rates):
    """Extract firing rates from a sim result and save them. """
    # Load sim result
    fpath_sim = _gen_model_path(model_name, postfix_sim)
    with open(fpath_sim, 'rb') as fid:
        sim_res = pkl.load(fid)
    # Extract rates
    pop_names = srp.get_pop_names(sim_res)
    pop_rate_data = {}
    for pop_name in pop_names:
        pop_rate_data[pop_name] = srp.get_pop_cell_rates(sim_res, pop_name)
    # Save rates
    fpath_out = fpath_sim = _gen_model_path(model_name, postfix_rates)
    with open(fpath_out, 'wb') as fid:
        pkl.dump(pop_rate_data, fid)


# Extract firing rate info
for name, info in models_info.items():
    print(f'Extracting rates for {name} model...')
    fpath_rates = _gen_model_path(name, '_pop_rates.pkl')
    if not os.path.exists(fpath_rates) or recalc_rates:
        fpath_sim = _gen_model_path(name, '_data.pkl')
        _extract_rate_data(name, '_data.pkl', '_pop_rates.pkl')
    with open(fpath_rates, 'rb') as fid:
        info['cell_rates'] = pkl.load(fid)
        
# Calculate rate histograms and averages
for name, info in models_info.items():
    info['avg_rates'], info['rate_hist'] = {}, {}
    for pop, rates in info['cell_rates'].items():
        info['avg_rates'][pop] = np.nanmean(rates)
        info['rate_hist'][pop] = np.histogram(rates, bins=bins, density=True)
        
pops_vis = ['L2e', 'L2i']
nx = 2
ny = 1

plt.figure()
for n, pop in enumerate(pops_vis):
    plt.subplot(ny, nx, n + 1)
    for model_name, info in models_info.items():
        h, b = info['rate_hist'][pop]
        plt.plot(b[:-1], h, label=model_name)
    plt.xlabel('Firing rate')
    plt.title(pop)
plt.subplot(ny, nx, 1)
plt.legend()

    

