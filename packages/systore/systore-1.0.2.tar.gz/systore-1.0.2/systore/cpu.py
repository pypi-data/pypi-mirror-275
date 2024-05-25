import psutil as _psutil
from functools import lru_cache

@lru_cache
def get_cpu_cores(): 
    """
    Returns the number of cpu cores in your computer.
    """
    return _psutil.cpu_count(logical=False)
@lru_cache
def get_virtual_cpu_cores(): 
    """
    Returns the number of virtual cpu cores in your computer.
    Virtual cores are used to make a cpu more like a GPU to increase its speed.
    """
    return _psutil.cpu_count(logical=True)

# optimize it by storing it in cache cuz its not like the user is changing the cpu while its running
@lru_cache
def get_max_cpu_speed():
    cpu_freq = _psutil.cpu_freq()
    return cpu_freq.max

@lru_cache
def get_min_cpu_speed():
    cpu_freq = _psutil.cpu_freq()
    return cpu_freq.min

def get_cpu_usage():
    cpu_freq = _psutil.cpu_freq()
    return cpu_freq.current
