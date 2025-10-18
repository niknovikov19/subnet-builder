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

    conns_split: dict[str | tuple[str, str], float] = \
        field(default_factory=dict)
    
    def prepare(self):
        # Convert conn keys in conns_split from str to tuple:
        # 'pop1, pop2' -> ('pop1', 'pop2')
        conns_split_new = {}
        for k, v in self.conns_split.items():
            if isinstance(k, str) and (',' in k):
                k_new = tuple(s.strip() for s in k.split(','))
            else:
                k_new = k
            conns_split_new[k_new] = v
        self.conns_split = conns_split_new

    #duplicate_active_pops: bool = False

    # conn. names or pre/post pop pairs
    #pops_inactive: list[str | tuple[str, str]]
    
    def save(self, fpath): pass
    def load(self, fpath): pass