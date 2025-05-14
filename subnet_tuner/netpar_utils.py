from .utils import to_list


def get_cond_pops(net_params: dict, conds: dict) -> list[str]:
    """Return a list of populations that meet the conditions conds. """
    # Note: could return a superset of the actual list
    if 'pop' in conds:
        return to_list(conds['pop'])
    elif 'cellType' in conds:
        pops = []
        for pop, par in net_params['popParams'].items():
            if 'cellType' in par:
                if par['cellType'] in to_list(conds['cellType']):
                    pops.append(pop)
        return pops
    else:
        s = f'Conditions should contain "pop" or "cellType"\n{conds}'
        #raise ValueError(s)
        print(s)
        return []

def get_conn_pops_presyn(net_params: dict, conn: str,
                          par_group: str = 'connParams') -> list[str]:
    """Get pre-synaptic populations of a (sub-)connection (from full model). """
    conds = net_params[par_group][conn]['preConds']
    return get_cond_pops(net_params, conds)
        
def get_conn_pops_postsyn(net_params: dict, conn: str,
                          par_group: str = 'connParams') -> list[str]:
    """"Get post-synaptic populations of a (sub-)connection (from full model). """
    conds = net_params[par_group][conn]['postConds']
    return get_cond_pops(net_params, conds)