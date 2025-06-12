import json
from pathlib import Path
import pickle as pkl
import sys
import warnings

import numpy as np

from netpyne import specs, sim

from subnet_tuner import (
    SubnetDesc, SubnetParamBuilder2,
    netpar_to_mermaid
)

# Force load the NEURON version with compiled modules
from neuron import h
nrn_path = Path(__file__).resolve().parent / 'nrnmech.dll'
h.nrn_load_dll(str(nrn_path))


warnings.simplefilter('once')

dirpath_work = Path(r'D:\WORK\Salvador\repo\subnet_tuner\test\model_PD2_L24_Izh2')

fpath_par_orig = dirpath_work / 'model.json'
with open(fpath_par_orig, 'r') as fid:
    par = json.load(fid)

# Load config
fpath_cfg = dirpath_work / 'cfg_sub.json'
with open(fpath_cfg, 'r') as fid:
    cfg_sub = json.load(fid)

# Subnet description
desc = SubnetDesc()
desc.pops_active = ['L2e', 'L2i']
desc.conns_frozen = []
for n, pop in enumerate(par['popParams']):
    desc.inp_surrogates[pop] = {
        'type': 'irregular',
        'rate': n * 10,
        'noise': 1.0
    }
desc.duplicate_active_pops = True

spb = SubnetParamBuilder2()
par_sub = spb.build(par, desc)

# Prepare
sim.initialize(simConfig=cfg_sub, netParams=par_sub)
sim.net.createPops()
sim.net.createCells()
sim.net.connectCells()
sim.net.addStims()

print('==== TURN ACTIVE CONNS ON ====')
spb.switch_active_conns(turn_on=1, net=sim.net)

print('==== TURN ACTIVE CONNS OFF ====')
spb.switch_active_conns(turn_on=0, net=sim.net)



