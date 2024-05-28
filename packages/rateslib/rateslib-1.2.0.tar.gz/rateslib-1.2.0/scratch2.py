from rateslib import *
import time

from rateslib.dual.dual import Dual as dpy
from rateslib.dual.dualrs import Dual as drs

from rateslib.dual.dual import _dsolve as dsolpy
from rateslib.dual import dual_solve as dsolrs

def time_op(label, func, *args):
    # start = time.time()
    # func(*args)
    # elapsed = time.time() - start
    # if abs(elapsed) < 1e-8:
    #     iters = int(1e4)
    # else:
    #     iters = min(int(2 / elapsed), 1)
    iters = 1

    start = time.time()
    for i in range(iters):
        func(*args)
    elapsed = (time.time() - start) / iters
    if elapsed < 1e-3:
        print(f"{label} took {elapsed*1000000:.3f}us / iters: {iters}")
    else:
        print(f"{label} took {elapsed * 1000:.6f}ms / iters: {iters}")

vars_rs = drs(0.0, [f"{i}" for i in range(50)], [])
vars_py = dpy(0.0, [f"{i}" for i in range(50)], [])

def cdrs(x):
    return drs.vars_from(vars_rs, x, vars=[], dual=[])

def cdpy(x):
    return dpy.vars_from(vars_py, x, vars=[], dual=[])

import numpy as np

A = np.random.rand(75, 75)
Ars = np.vectorize(cdrs)(A)
Apy = np.vectorize(cdpy)(A)

b = np.random.rand(75, 1)
brs = np.vectorize(cdrs)(b)
bpy = np.vectorize(cdpy)(b)

time_op("Numpy Linalg with Float", np.linalg.solve, A, b)
time_op("Python with Python Float / Dual:", dsolpy, A, bpy, False)
time_op("Python with Python Dual / Dual:", dsolpy, Apy, bpy, False)
time_op("Python with Rust Float / Dual:", dsolpy, A, bpy, False)
time_op("Python with Rust Dual / Dual:", dsolpy, Ars, brs, False)
time_op("Rust with Rust Float / Dual:", dsolrs, A, brs, False)
time_op("Rust with Rust Dual / Dual:", dsolrs, Ars, brs, False)
