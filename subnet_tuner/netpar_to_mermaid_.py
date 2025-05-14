from .netpar_utils import (
    get_conn_pops_presyn, get_conn_pops_postsyn
)

info_template = '''
<div style="position: relative; padding-top: 30px;">  
  <!-- your info text, absolutely positioned inside the container -->
  <div style="
      position: absolute;
      top: 0;
      right: 0;
      font-size: 0.8em;
      color: #666;
    ">
    {info}
  </div>
</div>

'''


def netpar_to_mermaid(net_params: dict, fpath_out: str,
                      info: str | None = None) -> None:    
    info_block = ''
    if info is not None:
        info = info.replace('\n', '<BR>')
        info_block = info_template.format(info=info)
    lines = ['```mermaid', 'graph LR']
    
    # Nodes
    for pop, params in net_params['popParams'].items():
        label_parts = [f"{pop}"]
        if "cellType" in params:
            label_parts.append(params['cellType'])
        if "cellModel" in params:
            label_parts.append(params['cellModel'])
        label = "<br/>".join(label_parts)
        lines.append(f'    {pop}["{label}"]')
    
    # Connections
    for conn in net_params['connParams']:
        pops_pre = get_conn_pops_presyn(net_params, conn)
        pops_post = get_conn_pops_postsyn(net_params, conn)
        for pre in pops_pre:
            for post in pops_post:
                lines.append(f'    {pre} -->|{conn}| {post}')
    
    lines.append('```')
    
    # Write to file
    with open(fpath_out, 'w') as f:
        f.write(info_block)
        f.write("\n".join(lines))