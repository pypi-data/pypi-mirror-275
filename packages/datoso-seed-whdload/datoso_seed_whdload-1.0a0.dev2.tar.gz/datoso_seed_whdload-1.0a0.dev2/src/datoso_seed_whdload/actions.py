from datoso_seed_whdload.dats import WhdloadDat

# ruff: noqa: ERA001

actions = {
    '{dat_origin}': [
        {
            'action': 'LoadDatFile',
            '_class': WhdloadDat,
        },
        {
            'action': 'DeleteOld',
        },
        {
            'action': 'Copy',
            'folder': '{dat_destination}',
        },
        {
            'action': 'SaveToDatabase',
        },
    ],
}

def get_actions():
    return actions
