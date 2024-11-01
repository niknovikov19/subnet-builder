import json

import matplotlib
matplotlib.use('Agg')  # to avoid graphics error on servers

from netpyne import sim, specs


#fpath_cfg = r"D:\WORK\Salvador\repo\A1_model_old\model\v34_batch56_0_0_cfg.json"
#fpath_par = (r"D:\WORK\Salvador\repo\A1_model_old\data\exp_subnet_L3_3s_replay"
#             r"\exp_subnet_L3_3s_replay_netParams_sub.json")

fpath_cfg = r"D:\WORK\Salvador\repo\subnet_tuner\test\model_PD2_L24_Izh2\cfg_sub.json"
fpath_par = (r"D:\WORK\Salvador\repo\subnet_tuner\test\model_PD2_L24_Izh2"
             r"\model_sub_(inp=replay).json")

with open(fpath_cfg, 'r') as fid:
    cfg_dict = json.load(fid)
#cfg = specs.SimConfig(cfg_dict['simConfig'])
cfg = specs.SimConfig(cfg_dict)

with open(fpath_par, 'r') as fid:
    netParams_sub = json.load(fid)
#netParams_sub = specs.NetParams(netParams_sub['net']['params'])
netParams_sub = specs.NetParams(netParams_sub)

cfg.singleCellPops = 1

# Prepare simulation
sim.initialize(simConfig=cfg, netParams=netParams_sub)
sim.net.createPops()               			# instantiate network populations
sim.net.createCells()              			# instantiate network cells based on defined populations
