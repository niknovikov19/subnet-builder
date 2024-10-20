import json
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
import common as cmn
from subnet_par_builder import SubnetParamBuilder, SubnetDesc


dirpath_work = Path(r'D:\WORK\Salvador\repo\subnet_tuner\test\model_PD2_L24_Izh2')

fpath_par_orig = dirpath_work / 'model.json'
with open(fpath_par_orig, 'r') as fid:
    par = json.load(fid)
    
# Subnet description
desc = SubnetDesc()
desc.pops_active = ['L2e', 'L2i', 'poissL2e', 'poissL2i']
desc.conns_frozen = []
desc.inp_surrogates['L4e'] = {'type': 'irregular', 'rate': 22, 'noise': 1}
desc.inp_surrogates['L4i'] = {'type': 'irregular', 'rate': 27, 'noise': 1}

spb = SubnetParamBuilder()
par_sub = spb.build(par, desc)

fpath_par_sub = dirpath_work / 'model_sub.json'
with open(fpath_par_sub, 'w') as fid:
    json.dump(par_sub, fid, cls=cmn.NumpyEncoder, indent=4)