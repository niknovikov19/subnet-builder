import json
from pathlib import Path

import pandas as pd

from subnet_tuner import (
    SubnetDesc, SubnetParamBuilder2,
    netpar_to_mermaid
)


exp_name = 'g_ouinp_wmult_0.02'

# Subnet description
desc = SubnetDesc()
desc.conns_frozen = 'all'
#desc.pops_active = 'all'
#subnet_postfix = 'all'
desc.pops_active = ['SOM4', 'IRE']
subnet_postfix = 'som4_ire'

dirpath_base = Path(__file__).resolve().parent / exp_name
fname_par_full = f'netParams_{exp_name}'
subnet_name = f'par_sub_{exp_name}_{subnet_postfix}'

# Read full netParams from json
with open(dirpath_base / (fname_par_full + '.json'), 'r') as f:
    par = json.load(f)['net']['params']

# Load target firing rates
target_rates = pd.read_csv(dirpath_base / 'target_rates.csv')
target_rates = target_rates.set_index('pop_name')['target_rate'].to_dict()

# Surrogate rates
for pop in par['popParams']:
    desc.inp_surrogates[pop] = {
        'type': 'irregular',
        'rate': target_rates[pop]
    }

# Build subnet
spb = SubnetParamBuilder2()
par_sub = spb.build(par, desc)

# Drop OU input params for non-active pops. and rename fields
par_sub['NoiseOUParams'] = {}
for pop, par in par_sub['NoiseConductanceParams'].items():
    if (desc.pops_active == 'all') or (pop in desc.pops_active):
        par_sub['NoiseOUParams'][pop] = {
            'mean': par['g0'],
            'sigma': par['sigma']
        }
par_sub.pop('NoiseConductanceParams')

# Save to json
#with open(dirpath_base / 'par_full.json', 'w') as f:
#    json.dump(par, f, indent=4)
with open(dirpath_base / f'{subnet_name}.json', 'w') as f:
    json.dump(par_sub, f, indent=4)

""" # Save original to mermaid
netpar_to_mermaid(par, dirpath_base / 'par_full.md')

# Save subnet to mermaid
info = ''
if desc.pops_active == 'all':
    info += 'Active: all'
else:
    info += 'Active: ' + ', '.join(desc.pops_active)
info += '\n'
if desc.conns_frozen == 'all':
    info += 'Frozen: all'
else:
    info += 'Frozen: ' + ', '.join(desc.conns_frozen)
netpar_to_mermaid(par_sub, dirpath_base / f'{subnet_name}.md', info) """
