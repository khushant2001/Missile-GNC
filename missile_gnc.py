import numpy as np
from control.matlab import *
import matplotlib.pyplot as plt

A = np.array([
    [-1.064, 1],
    [290.26, 0]
])
B = np.array([
    [-.25],
    [-331.40]
])
C = np.array([
    [-123.34, 0],
    [0,1]
])
D = np.array([
    [-13.51],
    [0]
])

Q = np.array([
    [1,0],
    [0,10]
])
R = np.array([
    [1]
])
sys = ss(A,B,C,D)
k,_,_ = lqr(sys,Q,R)
print(k)