
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


fpath_sim = r"D:\WORK\Salvador\repo\A1_model_old\data\exp_subnet_L3_3s\exp_subnet_L3_3s_data.pkl"

#with open(fpath_sim, 'rb') as fid:
#    sim_res = pkl.load(fid)

# Get spikes
pop_name = 'PV3'
spikes = srp.get_pop_spikes(sim_res, pop_name, combine_cells=False)
ncells = len(spikes)

# Filter spikes
t0 = 0.7
spikes = [s[s >= t0] for s in spikes]

ss = np.concatenate(spikes)
T = ss.max() - ss.min()
nspikes = np.array([len(s) for s in spikes])
rr = nspikes / T

surr = 1
if surr:
    for n, r in enumerate(rr):
        spikes[n] = gen_spikes(r=r, CV=0.7)

isi, cv2 = [], []
cv2_avg = np.full(ncells, np.nan)
for n, s in enumerate(spikes):
    isi_ = s[1:] - s[:-1]
    cv2_ = 2 * np.abs(isi_[1:] - isi_[:-1]) / (isi_[1:] + isi_[:-1])
    isi += list(isi_)
    cv2 += list(cv2_)
    cv2_avg[n] = np.mean(cv2_)
isi = np.array(isi)
cv2 = np.array(cv2)

#bins = np.linspace(0, 0.1, 50)
h, b = np.histogram(cv2, bins=20, density=True)
plt.figure()
plt.plot(b[1:], h)
plt.xlabel('CV2, local')
plt.ylabel('Probability')
plt.xlim(0, 2)

h, b = np.histogram(cv2_avg[~np.isnan(cv2_avg)], bins=10, density=True)
plt.figure()
plt.plot(b[1:], h)
plt.xlabel('CV2, avg')
plt.ylabel('Probability')
plt.xlim(0, 2)

plt.figure()
for s in spikes:
    d = s[1:] - s[:-1]
    d = np.log(d)
    plt.plot(d[:-1], d[1:], '.')
plt.xlabel('ISI, previous')
plt.ylabel('ISI, next')
