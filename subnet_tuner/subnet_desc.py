from dataclasses import dataclass, field
from typing import Literal


@dataclass
class SubnetDesc:
    """
    Description of a sub-network model.

    Attributes:
        pops_active (list | 'all'): pops that remain unchanged ("active")
        conns_frozen (list[str | tuple[str, str]] | 'all'): frozen conns between active pops.
            str - conn name; tuple[str, str] - pre/post pop pair of a conn.
        inp_surrogates (dict): params of spike generators that serve as
            surrogate replacements of frozen populations
    """    
    pops_active: list[str] | Literal['all'] = \
        field(default_factory=list)
    conns_frozen: list[str | tuple[str, str]] | Literal['all'] = \
        field(default_factory=list)
    inp_surrogates: dict = field(default_factory=dict)

    duplicate_active_pops: bool = False

    # conn. names or pre/post pop pairs
    #pops_inactive: list[str | tuple[str, str]]   
    
    def save(self, fpath): pass
    def load(self, fpath): pass