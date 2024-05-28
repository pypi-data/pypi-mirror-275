import sys
import subprocess
import time
import os
import os.path
import random


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


def on_mac() -> bool:
    return "DARWIN" in sys.platform.upper()

def on_win() -> bool:
    return "WIN32" in sys.platform.upper()

def on_lin() -> bool:
    return "LINUX" in sys.platform.upper()

def edit(filename):
    if "WIN32" in sys.platform.upper():
        subprocess.call(["notepad.exe", filename])
    else:
        subprocess.call(["nano", filename])


def create_temporary_file(prefix="tempfile", ext='') -> str:
    rnd = "".join([ str(random.randint(0,9)) for x in range(8)])
    if len(ext)>0:
        ext = '.' + ext
    filename = "%s-%d-%s%s" % (prefix, time.time_ns(), rnd, ext)
    full_filename:str = ''
    if on_win():
        full_filename = os.path.join("C:/Windows/Temp", filename)
    else:
        full_filename = os.path.join("/tmp", filename)

    if os.path.isfile(full_filename):
        raise Exception("Unable to create tmp file %s" % full_filename)

    with open(full_filename, 'w') as f:
        pass
    
    return full_filename
