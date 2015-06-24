import matplotlib.pyplot as plt
from scipy.integrate import odeint
from math import sqrt
from numpy import linspace

m1 = 0
m2 = 0
m3 = 0
x1 = 0
y1 = 0
x2 = 0
y2 = 0
x3 = 0
y3 = 0
G = 67428*(10**-11)

def func(X, t):
    x1 = X[1]
    y1 = X[3]
    x2 = X[5]
    y2 = X[7]
    x3 = X[9]
    y3 = X[11]
    x12 = x2 - x1
    x13 = x3 - x1
    x23 = x3 - x2
    y12 = y2 - y1
    y13 = y3 - y1
    y23 = y3 - y2
    k12 = (G*m1*m2)/(x12**2 + y12**2)
    k13 = (G*m1*m3)/(x13**2 + y13**2)
    k23 = (G*m2*m3)/(x23**2 + y23**2)
    
    

X0 = [Vx1, x1, Vy1, y, Vx2, x2, Vy2, y2, Vx3, x3, Vy3, y3]
x = odeint(func, X0, t)