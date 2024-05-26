import sys

def load_conf(args):
    res = {}
    res['os'] = ""

    if "DARWIN" in sys.platform.upper():
        res['os'] = res['os'] + 'm'

    if "WIN32" in sys.platform.upper():
        res['os'] = res['os'] + 'w'
    
    if "LINUX" in sys.platform.upper():
        res['os'] = res['os'] + 'l'

    if len(res['os']) != 1:
        res['os'] = "unknown"

    return res
