from subnet_par_builder import SubnetParamBuilder, SubnetDesc


par = {}
par['popParams'] = {}
par['connParams'] = {}
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

# Subnet description
desc = SubnetDesc()
desc.pops_active = ['P0', 'P1', 'P3']
desc.conns_frozen = []
for n in range(8):
    desc.inp_surrogates[f'P{n}'] = {'type': 'irregular', 'rate': n * 100}

spb = SubnetParamBuilder()
par_sub = spb.build(par, desc)
