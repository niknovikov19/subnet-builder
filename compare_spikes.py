# Compare firing rate distributions between several models

from contextlib import contextmanager
import os
from pathlib import Path
import pickle as pkl

import matplotlib
import matplotlib.pyplot as plt
import numpy as np 

import sim_res_parse_utils as srp


dirpath_data_root = Path(r'D:\WORK\Salvador\repo\A1_model_old\data')

models_info = {
    'full_10s': {'path': ('A1_paper', 'v34_batch56_10s')},
    #'L3_sub_poiss': {'path': ('exp_subnet_L3_8s_poiss_t=1-10', 'exp_subnet_L3_8s_poiss_t=1-10')},
    'L3_sub_rep_8s_1-10': {'path': ('exp_subnet_L3_8s_replay_t=1-10', 'exp_subnet_L3_8s_replay_t=1-10')},
    #'L3_sub_rep_jit_8s_1-10': {'path': ('exp_subnet_L3_8s_replay_jit_t=1-10', 'exp_subnet_L3_8s_replay_jit_t=1-10')}
    }
pops_vis = ['IT3', 'SOM3', 'PV3', 'VIP3', 'NGF3']
# =============================================================================
# models_info = {
#     'full_10s': {'path': ('A1_paper', 'v34_batch56_10s')},
#     'L2_sub_rep_8s_1-10': {'path': ('exp_subnet_L2_8s_replay_t=1-10', 'exp_subnet_L2_8s_replay_t=1-10')},
#     'L2_sub_rep_8s_0-10': {'path': ('exp_subnet_L2_8s_replay_t=0-10', 'exp_subnet_L2_8s_replay_t=0-10')}
#     }
# pops_vis = ['IT2', 'SOM2', 'PV2', 'VIP2', 'NGF2']
# =============================================================================

t0 = 1

recalc_rates = 0

bins = 10
#bins = np.linspace(0, 40, 10)


# =============================================================================
# @contextmanager
# def no_plt_close():
#     backend = matplotlib.get_backend()
#     #original_close = plt.close
#     #plt.close = lambda *args, **kwargs: None
#     plt.ioff()
#     yield
#     plt.ion()
#     #plt.close = original_close
#     matplotlib.use(backend)
# =============================================================================

def _gen_model_path(model_name, postfix):
    info = models_info[model_name]
    if isinstance(info['path'], str):
        fpath = dirpath_data_root / (info['path'] + postfix)
    else:
        fpath = dirpath_data_root / info['path'][0] / (info['path'][1] + postfix)
    return str(fpath)

def _extract_rate_data(model_name, postfix_sim, postfix_rates, t0=0):
    """Extract firing rates from a sim result and save them. """
    # Load sim result
    fpath_sim = _gen_model_path(model_name, postfix_sim)
    #with no_plt_close(), open(fpath_sim, 'rb') as fid:
    with open(fpath_sim, 'rb') as fid:
        sim_res = pkl.load(fid)
    # Extract rates
    pop_names = srp.get_pop_names(sim_res)
    pop_rate_data = {}
    for pop_name in pop_names:
        pop_rate_data[pop_name] = srp.get_pop_cell_rates(sim_res, pop_name, t0)
    # Save rates
    fpath_out = fpath_sim = _gen_model_path(model_name, postfix_rates)
    with open(fpath_out, 'wb') as fid:
        pkl.dump(pop_rate_data, fid)


# Extract firing rate info
for name, info in models_info.items():
    print(f'Extracting rates for {name} model...')
    postfix_rates = f'_pop_rates_(t0={t0}).pkl'
    fpath_rates = _gen_model_path(name, postfix_rates)
    if not os.path.exists(fpath_rates) or recalc_rates:
        fpath_sim = _gen_model_path(name, '_data.pkl')
        _extract_rate_data(name, '_data.pkl', postfix_rates, t0)
    with open(fpath_rates, 'rb') as fid:
        info['cell_rates'] = pkl.load(fid)
        
# Calculate rate histograms and averages
for name, info in models_info.items():
    info['avg_rates'], info['rate_hist'] = {}, {}
    for pop, rates in info['cell_rates'].items():
        info['avg_rates'][pop] = np.nanmean(rates)
        info['rate_hist'][pop] = np.histogram(rates, bins=bins, density=True)
        
nx = 3
ny = 2

plt.figure()
for n, pop in enumerate(pops_vis):
    plt.subplot(ny, nx, n + 1)
    for model_name, info in models_info.items():
        if pop in info['rate_hist']:
            h, b = info['rate_hist'][pop]
            style = '-'
        else:
            h, b = info['rate_hist'][pop + 'frz']
            style = '--'
        plt.plot(b[:-1], h, style, label=model_name)
    plt.title(pop)
plt.subplot(ny, nx, 1)
plt.legend()
for n in range(nx):
    plt.subplot(ny, nx, (ny - 1) * nx + 1 + n)
    plt.xlabel('Firing rate')

    

