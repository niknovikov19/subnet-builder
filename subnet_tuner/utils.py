import copy

import numpy as np


def deepcopy2(x):
    if isinstance(x, dict):
        return {key: deepcopy2(val) for key, val in x.items()}
    elif isinstance(x, list):
        return [deepcopy2(val) for val in x]
    elif hasattr(x, '__dict__'):
        y = copy.copy(x)
        for attr_name in x.__dict__:
            attr_val = getattr(x, attr_name)
            attr_val = deepcopy2(attr_val)
            setattr(y, attr_name, attr_val)
        return y
    else:
        return x

def to_list(x):
    return np.atleast_1d(x).tolist()

def lists_intersect(list1, list2):
    return bool(set(list1) & set(list2))