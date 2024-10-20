import json
from pathlib import Path

from netpyne import specs, sim


dirpath_work = Path(r'D:\WORK\Salvador\repo\subnet_tuner\test\model_PD2_L24_Izh2')

# Load model params
fpath_par = dirpath_work / 'model_sub.json'
with open(fpath_par, 'r') as fid:
    par_ = json.load(fid)

# Load config
fpath_cfg = dirpath_work / 'cfg_sub.json'
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

sim.saveData()
sim.analysis.plotData()         			# plot spike raster etc

# Visualize the result
pop_names = cfg_['recordCellsSpikes']
sim.analysis.plotRaster(orderInverse=True, include=pop_names)
sim.analysis.plotSpikeStats(include=pop_names, stats=['rate', 'isicv'])
    
    
    