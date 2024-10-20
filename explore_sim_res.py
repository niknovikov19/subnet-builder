import collections
from pathlib import Path
import pickle as pkl

from netpyne import sim, specs
from netpyne.analysis.utils import colorList
import numpy as np
from matplotlib import pyplot as plt
#import pandas as pd


dirpath_work = Path(r'D:\WORK\Salvador\repo\subnet_tuner\test\model_PD2_L24_Izh2')

fname_res = 'sim_res_data.pkl'
#fname_res = 'sim_res_sub_data.pkl'


fpath_in = str(dirpath_work / fname_res)

with open(fpath_in, 'rb') as fid:
    sim_res = pkl.load(fid)
    
#sim.initialize()
sim.loadAll(fpath_in, instantiate=False)

sim.analysis.plotRaster(orderInverse=True, timeRange=(0, 500))#, include=include)
#plt.xlim(1500, 3000)

#sim.analysis.plotSpikeStats(include=include, stats=['rate'], timeRange=(1500, 3000))
#sim.analysis.plotSpikeStats(include=include, stats=['rate'])
sim.analysis.plotSpikeStats(include=['eachPop'], stats=['rate'])
#plt.xlim((0, 200))
