import json
from pathlib import Path
from time import time
import sys

from netpyne import specs, sim
import numpy as np

sys.path.append(str(Path(__file__).resolve().parents[2]))
import common as cmn


netParams = specs.NetParams()
cfg = specs.SimConfig()


############################################################
# Run options
############################################################

Tsim = 500

cfg.seeds['stim'] = 3
cfg.duration = Tsim
cfg.dt = 0.05
cfg.verbose = False
cfg.seeds['m'] = 123
#cfg.printPopAvgRates = True
#cfg.printRunTime = 1
cfg.simLabel = "SIM1"
 
cfg.recordCellsSpikes = ['L2e', 'L2i', 'L4e', 'L4i']


###########################################################
#  Network Constants
###########################################################

scale = 0.01

# Probability of connection
C = np.array([[0.20, 0.33, 0.08, 0.16],
              [0.26, 0.27, 0.06, 0.10],
              [0.015, 0.012, 0.2, 0.27],
              [0.14, 0.006, 0.16, 0.14]])

# Population names
pop_names = ['L2e', 'L2i', 'L4e', 'L4i']
L = pop_names

# Input rates
InpPoiss = np.array([65, 110, 115, 280])

# Population sizes
N_Full = np.array([20683, 5834, 21915, 5479]).reshape((1, 4))
N_ = (scale * N_Full).astype(int).ravel()

# Divergence
K = (scale * (np.log(1. - C) / np.log(1. - 1. / (N_Full.T @ N_Full))) / N_Full)

w_p = 0.006

############################################################
# NetPyNE Network Parameters (netParams)
############################################################

netParams.delayMin_e = 1.5
netParams.ddelay = 0.5
netParams.delayMin_i = 0.75
netParams.weightMin = w_p
netParams.dweight = 0.1

############################################################
# Cell parameters
############################################################

# Cell (RS)
netParams.cellParams['PYR'] = {
    "conds": {},
    "secs": {
        "soma": {
            "geom": {"L": 10.0, "nseg": 1, "diam": 10.0, "Ra": 35.4, "cm": 31.831},
            "topol": {},
            "mechs": {},
            "pointps": {
                "Izhi2007b_0": {
                    "mod": "Izhi2007b",
                    "loc": 0.5,
                    "C": 1.0,
                    "k": 0.7,
                    "vr": -60.0,
                    "vt": -40.0,
                    "vpeak": 35.0,
                    "a": 0.03,
                    "b": -2.0,
                    "c": -50.0,
                    "d": 100.0,
                    #"Iin": -450.0,
                    "Iin": -50.0,
                    "celltype": 1.0,
                    "alive": 1.0,
                    "cellid": -1.0
                }
            }
        }
    },
    "secLists": {},
    "globals": {}
}
                
# Cell (FS)
netParams.cellParams['FS'] = {
    "conds": {},
    "secs": {
        "soma": {
            "geom": {"L": 10.0, "nseg": 1, "diam": 10.0, "Ra": 35.4, "cm": 31.831},
            "topol": {},
            "mechs": {},
            "pointps": {
                "Izhi2007b_0": {
                    "mod": "Izhi2007b",
                    "loc": 0.5,
                    "C": 0.2,
                    "k": 1.0,
                    "vr": -55.0,
                    "vt": -40.0,
                    "vpeak": 25.0,
                    "a": 0.2,
                    "b": -2.0,
                    "c": -45.0,
                    "d": -55.0,
                    #"Iin": -400.0,
                    "Iin": -25.0,
                    "celltype": 5.0,
                    "alive": 1.0,
                    "cellid": -1.0
                }
            }
        }
    },
    "secLists": {},
    "globals": {}
}
                
############################################################
# Populations parameters
############################################################

# Population locations
# (from Schmidt et al 2018, PLoS Comp Bio, Macaque V1)
netParams.sizeX = 300 # x-dimension (horizontal length) size in um
netParams.sizeY = 1470 # y-dimension (vertical height or cortical depth) size in um
netParams.sizeZ = 300 # z-dimension (horizontal depth) size in um
netParams.shape = 'cylinder' # cylindrical (column-like) volume

popDepths = [[0.08, 0.27], [0.08, 0.27], [0.27, 0.58], [0.27, 0.58],
             [0.58, 0.73], [0.58, 0.73], [0.73, 1.0], [0.73, 1.0]]

pop_types = {'L2e': 'PYR', 'L2i': 'FS', 'L4e': 'PYR', 'L4i': 'FS'}

# Create populations
for i, pop_name in enumerate(pop_names):
    netParams.popParams[pop_name] = {
                'cellType': pop_types[L[i]],
                'numCells': int(N_[i]),
                }

############################################################
# Connectivity parameters
############################################################

# Synaptic mechanisms
EAMPA = 0
EGABAA = -70                
tauAMPA = 2
tauGABAA = 5
netParams.synMechParams['AMPA']  = {
        'mod': 'ExpSyn', 'tau': tauAMPA, 'e': EAMPA}
netParams.synMechParams['GABAA'] = {
        'mod': 'ExpSyn', 'tau': tauGABAA, 'e': EGABAA}
        
for r, pop_name_post in enumerate(pop_names):
    for c, pop_name_pre in enumerate(pop_names):
        ww = 'max(0, weightMin + dweight * weightMin * normal(0, 1))'
        de = 'max(0.1, delayMin_e + normal(0, ddelay * delayMin_e))'
        di = 'max(0.1, delayMin_i + normal(0, ddelay * delayMin_i))'
        
        if (c % 2) == 0:
            d = de
            if c == 2 and r == 0:
                w = f'2 * {ww}'
            else:
                w = f'{ww}'
            syn_mech = 'AMPA'
        else:
            d = di
            w = w = f'4 * {ww}'
            syn_mech = 'GABAA'
        
        conn_name = pop_name_pre + '->' + pop_name_post
        netParams.connParams[conn_name] = {
            'preConds': {'pop': pop_name_pre},
            'postConds': {'pop': pop_name_post},
            'divergence': K[r, c],
            'weight': ww,
            'delay': d,
            'synMech': syn_mech
            }

############################################################
# External input parameters
############################################################

for r, pop_name in enumerate(pop_names):
    netParams.popParams['poiss' + pop_name] = {
        'numCells': N_[r], 
        'cellModel': 'NetStim',
        'rate': InpPoiss[r],   
        'start': 0.0, 
        'noise': 1.0, 
        'delay': 0
        }		
    auxConn = np.array([range(0, N_[r], 1), range(0, N_[r], 1)])
    netParams.connParams['poiss->' + pop_name] = {
        'preConds': {'pop': 'poiss' + pop_name},  
        'postConds': {'pop': pop_name},
        'connList': auxConn.T,   
        #'weight': 'max(0, weightMin+0.017*normal(0,1))',
        'weight': 'max(0, weightMin+weightMin*dweight*normal(0,1))',
        #'weight': w_p,
        #'weight': 'max(0, weightMin)',
        'delay': 0.5,
        'synMech': 'AMPA',
        'synsPerConn': 1
        }

############################################################
# Save the model
############################################################

dirpath_out = Path(r'D:\WORK\Salvador\repo\subnet_tuner\test\model_PD2_L24_Izh2')

# Params
par = netParams.todict()
fpath_par = dirpath_out / 'model.json'
with open(fpath_par, 'w') as fid:
    json.dump(par, fid, cls=cmn.NumpyEncoder, indent=4)
    
# Config
cfg_ = cfg.todict()
fpath_cfg = dirpath_out / 'cfg.json'
with open(fpath_cfg, 'w') as fid:
    json.dump(cfg_, fid, cls=cmn.NumpyEncoder, indent=4)

