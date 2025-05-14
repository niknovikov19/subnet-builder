# Compare firing rate distributions between several models

from contextlib import contextmanager
import json
import os
from pathlib import Path
import pickle as pkl

import matplotlib
import matplotlib.pyplot as plt
import numpy as np 

import sim_res_parse_utils as srp


dirpath_root = Path(r'D:\WORK\Salvador\repo\A1_model_old\data')

exp_name = 'exp_batch_subnet_layers'

#job_idx = [0, 1, 2]
#job_idx = [3, 4, 5]
#job_idx = [6, 7, 8]
job_idx = [7]

recalc_rates = 0

bins = 5
#bins = np.linspace(0, 40, 10)


dirpath_exp = dirpath_root / exp_name

# Read configs
job_info = {}
for job_id in job_idx:
    cfg_path = dirpath_exp / f'{exp_name}_{job_id:05d}_cfg.json'
    with open(cfg_path, 'r') as fid:
        cfg = json.load(fid)['simConfig']
    job_info[job_id] = {
        'inp_type': cfg['subnet_par']['inp_type'],
        'pops': cfg['subnet_par']['pops_active'],
        'layer': 'L' + cfg['subnet_par']['pops_active'][0][-1]
    }
    if job_info[job_id]['pops'] != job_info[job_idx[0]]['pops']:
        raise ValueError('Pop. groups should be the same')

# Subfolder and filename base
models_info = {}
models_info['full_10s'] = {'path': ('A1_paper', 'v34_batch56_10s'),
                           'tlim': (1, 9)}
for job_id, job in job_info.items():
    model_name = f'{job["layer"]}_sub_{job["inp_type"]}'
    models_info[model_name] = {'path': (exp_name, f'{exp_name}_{job_id:05d}'),
                               'tlim': (0, 8)}

def _gen_model_path(model_name, postfix):
    model_path = models_info[model_name]['path']
    fpath = dirpath_root / model_path[0] / (model_path[1] + postfix)
    return str(fpath)

def _extract_rate_data(model_name, postfix_sim, postfix_rates, postfix_spikes,
                       tlim):
    """Extract firing rates from a sim result and save them. """
    # Load sim result
    fpath_sim = _gen_model_path(model_name, postfix_sim)
    #with no_plt_close(), open(fpath_sim, 'rb') as fid:
    with open(fpath_sim, 'rb') as fid:
        sim_res = pkl.load(fid)
    # Extract rates
    pop_names = srp.get_pop_names(sim_res)
    pop_rate_data, spikes = {}, {}
    for pop_name in pop_names:
        pop_rate_data[pop_name] = srp.get_pop_cell_rates(
            sim_res, pop_name, tlim[0], tlim[1])
        spikes[pop_name] = srp.get_pop_spikes(
            sim_res, pop_name, combine_cells=False, t0=tlim[0], tmax=tlim[1])
    # Save rates
    fpath_out_rates = _gen_model_path(model_name, postfix_rates)
    with open(fpath_out_rates, 'wb') as fid:
        pkl.dump(pop_rate_data, fid)
    # Save spikes
    fpath_out_spikes = _gen_model_path(model_name, postfix_spikes)
    with open(fpath_out_spikes, 'wb') as fid:
        pkl.dump(spikes, fid)

# Extract firing rate info
for name, info in models_info.items():
    print(f'Extracting rates for {name} model...')
    tlim = info['tlim']
    postfix_rates = f'_pop_rates_(tlim={tlim[0]}-{tlim[1]}).pkl'
    postfix_spikes = f'_spikes_(tlim={tlim[0]}-{tlim[1]}).pkl'
    fpath_rates = _gen_model_path(name, postfix_rates)
    fpath_spikes = _gen_model_path(name, postfix_spikes)
    if ~os.path.exists(fpath_rates) or ~os.path.exists(fpath_spikes) or recalc_rates:
        _extract_rate_data(name, '_data.pkl', postfix_rates, postfix_spikes, tlim)
    with open(fpath_rates, 'rb') as fid:
        info['cell_rates'] = pkl.load(fid)
    with open(fpath_spikes, 'rb') as fid:
        info['spikes'] = pkl.load(fid)
        
# Calculate rate histograms and averages
for name, info in models_info.items():
    info['avg_rates'], info['rate_hist'] = {}, {}
    for pop, rates in info['cell_rates'].items():
        info['avg_rates'][pop] = np.nanmean(rates)
        info['rate_hist'][pop] = np.histogram(rates, bins=bins, density=True)

need_plot_r_sorted = 1
need_plot_hist = 0
        
nx = 3
ny = 2

#pops_vis = job_info[job_idx[0]]['pops']
#pops_vis = ['IT3', 'SOM3', 'PV3', 'VIP3', 'NGF3']
pops_vis = ['IT2', 'SOM2', 'PV2', 'VIP2', 'NGF2']
#pops_vis = ['IT5A', 'CT5A', 'SOM5A', 'PV5A', 'VIP5A', 'NGF5A']

if need_plot_r_sorted:
    plt.figure()
    for n, pop in enumerate(pops_vis):
        plt.subplot(ny, nx, n + 1)
        for model_name, info in models_info.items():
            if pop in info['rate_hist']:
                rr = info['cell_rates'][pop]
            else:
                rr = info['cell_rates'][pop + 'frz']
            plt.plot(np.sort(rr), '.', label=model_name)
        plt.title(pop)
    plt.subplot(ny, nx, 1)
    plt.legend()
    for n in range(ny):
        plt.subplot(ny, nx, n * nx + 1)
        plt.ylabel('Firing rate')
    for n in range(nx):
        plt.subplot(ny, nx, (ny - 1) * nx + 1 + n)
        plt.xlabel('Neuron #')

if need_plot_hist:
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


#fpath = r"D:\WORK\Salvador\repo\A1_model_old\data\A1_paper\v34_batch56_10s_spikes_(t=1-10).pkl"
#with open(fpath, 'rb') as fid:
#    S = pkl.load(fid)

pop = 'PV2'
s1 = models_info['full_10s']['spikes'][pop]
s2 = models_info['L4_sub_spike_replay']['spikes'][pop + 'frz']
ss = [s1, s2]
for n, s in enumerate(ss):
    ss[n] = [1000 * (s_ + 1) for s_ in s]
ss2 = ss.copy()

for n, s in enumerate(ss2):
    idx = np.argsort([len(s_) for s_ in s])
    ss2[n] = [s[m] for m in idx]

fpath = (r"D:\WORK\Salvador\repo\A1_model_old\data\exp_subnet_L3_8s_replay_t=1-10"
         r"\exp_subnet_L3_8s_replay_t=1-10_netParams_sub.json")
with open(fpath, 'r') as fid:
    par = json.load(fid)
    s3 = par['net']['params']['popParams'][pop + 'frz']['spkTimes']

