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


x12 = x2 - x1
x13 = x3 - x1
x23 = x3 - x2

y12 = y2 - y1
y13 = y3 - y1
y23 = y3 - y2