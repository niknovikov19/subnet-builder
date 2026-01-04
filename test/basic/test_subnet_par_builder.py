import json
from pathlib import Path

from subnet_tuner import (
    SubnetDesc, SubnetParamBuilder2,
    netpar_to_mermaid
)


par = {}
par['popParams'] = {}
par['connParams'] = {}
par['subConnParams'] = {}
par['meta'] = 'META'

# Populations
# P0, P1, P2, P3 with celltype C0
# P4, P5, P6, P7 with celltype C1
for n in range(8):
    par['popParams'][f'P{n}'] = {
        'cellModel': 'HH', 'ynormRange': (-n ,n), 'density': n * 10}
for n in range(0, 4):
    par['popParams'][f'P{n}']['cellType'] = 'C0'
for n in range(4, 8):
    par['popParams'][f'P{n}']['cellType'] = 'C1'

# Connections
par['connParams']['C0->P4'] = {
    'preConds': {'cellType': 'C0'}, 'postConds': {'pop': 'P4'}, 'weight': -0.4}
par['connParams']['P0->C1'] = {
    'preConds': {'pop': 'P0'}, 'postConds': {'cellType': 'C1'}, 'weight': -0.1}
par['connParams']['P1->P5'] = {
    'preConds': {'pop': 'P1'}, 'postConds': {'pop': 'P5'}, 'weight': 1.5}
par['connParams']['P5->P1'] = {
    'preConds': {'pop': 'P5'}, 'postConds': {'pop': 'P1'}, 'weight': 5.1}
par['connParams']['P23->P67'] = {
    'preConds': {'pop': ['P2', 'P3']}, 'postConds': {'pop': ['P6', 'P7']}, 'weight': 23.67}
par['connParams']['P6->P23'] = {
    'preConds': {'pop': 'P6'}, 'postConds': {'pop': ['P2', 'P3']}, 'weight': 6.23}
par['connParams']['P67->P3'] = {
    'preConds': {'pop': ['P6', 'P7']}, 'postConds': {'pop': 'P3'}, 'weight': 67.3}

# Sub-connections
par['subConnParams']['C0->C1'] = {
    'preConds': {'cellType': 'C0'}, 'postConds': {'cellType': 'C1'}}
# Sub-connections
par['subConnParams']['P123->C1'] = {
    'preConds': {'pop': ['P1', 'P2', 'P3']}, 'postConds': {'cellType': 'C1'}}
par['subConnParams']['C0->P456'] = {
    'preConds': {'cellType': 'C0'}, 'postConds': {'pop': ['P4', 'P5', 'P6']}}

# Subnet description
desc = SubnetDesc()
desc.pops_active = ['P1', 'P3', 'P4', 'P5']
#desc.pops_active = ['P0', 'P7', 'P3']
#desc.pops_active = 'all'
desc.conns_frozen = ['C0->P4', 'P1->P5']
#desc.conns_frozen = 'all'
#desc.conns_frozen = [('P3', 'P4')]
#desc.conns_frozen = []
#desc.conns_split = {('P1', 'P5'): 0.2, ('P5, P1'): 0.1}
for n in range(8):
    desc.inp_surrogates[f'P{n}'] = {'type': 'irregular', 'rate': n * 100}
desc.duplicate_active_pops = False
subnet_name = 'par_sub_8'

# Build subnet
spb = SubnetParamBuilder2()
par_sub = spb.build(par, desc)

""" print('--------')
spb.switch_active_conns(True)
print('--------')
spb.switch_active_conns(False) """

dirpath_base = Path(__file__).resolve().parent

# Save to json
with open(dirpath_base / 'par.json', 'w') as f:
    json.dump(par, f, indent=4)
with open(dirpath_base / f'{subnet_name}.json', 'w') as f:
    json.dump(par_sub, f, indent=4)

# Save original to mermaid
netpar_to_mermaid(par, dirpath_base / 'par.md')

# Save subnet to mermaid
info = 'Active: ' + ', '.join(desc.pops_active)
#info += '\nFrozen: ' + ', '.join(desc.conns_frozen)
netpar_to_mermaid(par_sub, dirpath_base / f'{subnet_name}.md', info)
