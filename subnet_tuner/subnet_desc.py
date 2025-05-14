from dataclasses import dataclass, field
from typing import Dict, List, Literal


@dataclass
class SubnetDesc:
    """
    Description of a sub-network model.

    Attributes:
        pops_active (list | 'all'): pops that remain unchanged ("active")
        conns_frozen (list | 'all'): conns between active pops that are frozen
        inp_surrogates (dict): params of spike generators that serve as
            surrogate replacements of frozen populations
    """    
    pops_active: list | Literal['all'] = field(default_factory=list)
    conns_frozen: list | Literal['all'] = field(default_factory=list)
    inp_surrogates: dict = field(default_factory=dict)
    
    def save(self, fpath): pass
    def load(self, fpath): pass