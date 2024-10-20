import json
from pathlib import Path
import sys

from netpyne import specs, sim

sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
import common as cmn
from subnet_par_builder import SubnetParamBuilder, SubnetDesc


dirpath_work = Path(r'D:\WORK\Salvador\repo\subnet_tuner\test\model_PD2_L24_Izh2')

#model_desc = ('model.json', 'cfg.json', 'sim_res')
model_desc = ('model_sub.json', 'cfg_sub.json', 'sim_res_sub')


# Load model params
fpath_par = dirpath_work / model_desc[0]
with open(fpath_par, 'r') as fid:
    par_ = json.load(fid)
    
# Load config
fpath_cfg = dirpath_work / model_desc[1]
with open(fpath_cfg, 'r') as fid:
    cfg_ = json.load(fid)

# Prepare
sim.initialize(simConfig=cfg_, netParams=par_)
sim.net.createPops()               			# instantiate network populations
sim.net.createCells()              			# instantiate network cells based on defined populations
sim.net.connectCells()            			# create connections between cells based on params
sim.net.addStims() 							# add network stimulation

# Run
sim.setupRecording()              			# setup variables to record for each cell (spikes, V traces, etc)
sim.runSim()                      			# run parallel Neuron simulation  
sim.gatherData()                  			# gather spiking data and cell info from each node

# Save the result
sim.cfg.savePickle = 1
fpath_res = str(dirpath_work / model_desc[2])
sim.saveData(include=['netParams', 'simData', 'net'], filename=fpath_res)
#sim.analysis.plotData()         			# plot spike raster etc

# Visualize the result
#pop_names = ['L2e', 'L2i', 'L4e', 'L4i']
#sim.analysis.plotRaster(orderInverse=True, include=pop_names)
#sim.analysis.plotSpikeStats(include=pop_names, stats=['rate', 'isicv'])
    
    
    