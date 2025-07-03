import regex as re

class Workspace:
    name = 'UNSET'
    id = 0
    monitor_name = 'UNSET'
    monitor_id = 0
    windows = 0
    has_fullscreen = 0
    last_window = ''
    last_window_title = ''
    is_persistent = 0


def parse_hyprland_reply(input_string):
    # Split the input string into lines
    lines = input_string.strip().split('\n')
    result = {}
    current_workspace = None

    for line in lines:
        if line == '': continue
        # Check if the line is a workspace header
        if not line.startswith('\t'):
            # Extract the workspace ID and create a new dictionary for it
            current_workspace = line.split(':')[0].strip()
            result[current_workspace] = {}
        else:
            # This line is a key-value pair
            key_value = line.strip().split(':', 1)
            if len(key_value) == 2:
                key = key_value[0].strip()
                value = key_value[1].strip()
                result[current_workspace][key] = value
    return result


def _parse_workspace_entry(entry: str):
    workspace = Workspace()
    lines = entry.split('\n')
    header = lines.pop(0)
    # Extract Name
    match = re.search('(?<=\().*(?=\))', header)
    if match: workspace.name = match.group()
    # Extract ID
    match = re.search('(?<=workspace ID ).*(?= \()', header)
    if match: workspace.id = int(match.group())
    # Extract Monitor Name
    match = re.search('(?<=on monitor ).*(?=:)', header)
    if match: workspace.monitor_name = match.group()

    for line in lines:
        property = line.strip().split(':')
        name = property[0].strip()
        value = property[1].strip()
        match name:
            case 'monitorID': workspace.monitor_id = int(value)
            case 'windows': workspace.windows = int(value)
            case 'hasfullscreen': workspace.has_fullscreen = int(value)
            case 'lastwindow': workspace.last_window = value
            case 'last_window_title': workspace.last_window_title = value
            case 'ispersistent': workspace.is_persistent = int(value)
    return workspace

def _parse_workspaces_reply(reply) -> list:
    reply_string = reply.decode('utf-8')
    entries = reply_string.split('\n\n')
    entries.pop(-1)
    print(entries)
    workspaces = []
    for entry in entries:
        workspaces.append(_parse_workspace_entry(entry))
    return workspaces

## Text in Parenthesis: /(?<=\().*(?=\))/gm
## Workspace ID: (?<=workspace ID ).*(?= \() 
## __Monitor Name: (?<=on monitor ).*(?=:)  

