
import os
from pathlib import Path
import pickle as pkl

import matplotlib.pyplot as plt
import numpy as np 

import sim_res_parse_utils as srp


def gen_spikes(r, CV, T=3):
    mean_ISI = 1 / r
    spike_times = []
    current_time = 0.0
    while current_time < T:
        if CV == 0:
            ISI = mean_ISI
        else:
            shape = 1 / CV**2
            scale = mean_ISI / shape
            ISI = np.random.gamma(shape, scale)
        current_time += ISI
        if current_time < T:
            spike_times.append(current_time)
    return np.array(spike_times)


#fpath_sim = r"D:\WORK\Salvador\repo\A1_model_old\data\exp_subnet_L3_3s\exp_subnet_L3_3s_data.pkl"
fpath_sim = r"D:\WORK\Salvador\repo\A1_model_old\data\A1_paper\v34_batch56_10s_data.pkl"

pop_name = 'VIP3'

#tlim = (1, 4)
tlim = (1, 10)

CV_surr = 0.7

need_reload = 0
use_surrogate = 0


if need_reload:
    with open(fpath_sim, 'rb') as fid:
        sim_res = pkl.load(fid)

# Get spikes
spikes = srp.get_pop_spikes(sim_res, pop_name, combine_cells=False)
ncells = len(spikes)

# Filter spikes
spikes = [s[(s >= tlim[0]) & (s <= tlim[1])] for s in spikes]

#ss = np.concatenate(spikes)

# Firing rates
T = tlim[1] - tlim[0]
nspikes = np.array([len(s) for s in spikes])
rr = nspikes / T

if use_surrogate:
    for n, r in enumerate(rr):
        spikes[n] = gen_spikes(r=r, CV=CV_surr)

def calc_cv2(isi, avg=True):
    isi = np.array(isi)
    cv2 = 2 * np.abs(isi[1:] - isi[:-1]) / (isi[1:] + isi[:-1])
    if avg:
        cv2 = np.nanmean(cv2)
    return cv2

def nanhist(x, *args, **kwargs):
    x = np.array(x)
    x = x[~np.isnan(x)]
    return np.histogram(x, *args, **kwargs)
    
# ISI statistics (CV2, ...) for individual cells
z = np.full(ncells, np.nan)
cv2 = z.copy()
for n, s in enumerate(spikes):
    isi_ = s[1:] - s[:-1]
    cv2[n] = calc_cv2(isi_)
    
# Pooled ISI statistics
isi_all = [s[1:] - s[:-1] for s in spikes]
cv2_pooled = np.concatenate([calc_cv2(isi_, avg=False) for isi_ in isi_all])
isi_pooled = np.concatenate(isi_all)

plt.figure()
cy, cx = 2, 2

# Rate histogram
plt.subplot(cy, cx, 1)
h, b = nanhist(rr, bins=20, density=True)
plt.plot(b[1:], h)
plt.xlabel('Firing rate')
plt.ylabel('Probability')
plt.title(f'{pop_name}, t={tlim[0]}-{tlim[1]}')
plt.xlim(8, 32)

# CV2 histogram
plt.subplot(cy, cx, 2)
h, b = nanhist(cv2, bins=10, density=True)
plt.plot(b[1:], h)
plt.xlabel('CV2')
plt.xlim(0, 2)

plt.subplot(cy, cx, 3)
h, b = nanhist(cv2_pooled, bins=20, density=True)
plt.plot(b[1:], h)
plt.xlabel('CV2, pooled')
plt.ylabel('Probability')
plt.xlim(0, 2)

plt.subplot(cy, cx, 4)
for isi_ in isi_all:
    d = np.log(isi_)
    plt.plot(d[:-1], d[1:], '.')
plt.xlabel('ISI, previous')
plt.ylabel('ISI, next')
