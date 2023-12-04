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

# Defining Q and R matrices to select weights on the states and input.
Q = np.array([
    [1,0],
    [0,.1]
])
R = np.array([
    [.01]
])
sys = ss(A,B,C,D)
k,_,_ = lqr(sys,Q,R)

print("Eigenvalues of the system are = ", np.linalg.eig(A)[0])
print("LQR gain for the system = ",k)

# Finding the kalman gain 
# The error between actual state and estimated state is defined as e_dot = [A - C*k]*e
pole_position = [-50,-100]
ke = place(A,C,pole_position)
print("Kalman gain for the system = ", ke)