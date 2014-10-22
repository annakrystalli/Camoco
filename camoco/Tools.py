import os
import sys
import time
import re
import functools

from itertools import chain
from camoco.Locus import *

def memoize(obj):
    cache = obj.cache = {}

    @functools.wraps(obj)
    def memoizer(*args, **kwargs):
        # This wraps the calling of the memoized object
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = obj(*args, **kwargs)
        return cache[key]
    return memoizer


def log(msg,*args):
    print("[LOG]",time.ctime(), '-', msg.format(*args),file=sys.stderr)

def ext(filename):
    return os.path.join(os.path.expanduser("~/MetaboloCOB/"+filename))

def B73_eq_Mo17(snp,HM):
    genotypes = HM.genotypes(snp,accessions=['B73','MO17'])
    if genotypes[0] == genotypes[1]:
        return True
    else:
        return False
