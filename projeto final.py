import matplotlib.pyplot as plt
from scipy.integrate import odeint
from math import sqrt
from numpy import linspace

m1 = 55000000
m2 = 850000000
m3 = 650000000
x1 = 500000
y1 = 600000
x2 = 800000
y2 = 900000
x3 = 700000
y3 = 700000
G = 67428*(10**-11)
Vx1 = 3000
Vy1 = 3200
Vx2 = 1000
Vy2 = 4500
Vx3 = 6000
Vy3 = 6000

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
    F12x = k12 * (x12/((sqrt(x12**2+y12**2)))) 
    F12y = k12 * (y12/((sqrt(x12**2+y12**2))))  
    F13x = k13 * (x13/((sqrt(x13**2+y13**2))))  
    F13y = k13 * (x13/((sqrt(x13**2+y13**2))))
    F23x = k23 * (x23/((sqrt(x23**2+y23**2))))  
    F23y = k23 * (x23/((sqrt(x23**2+y23**2))))
    dVx1dt = (F12x + F13x)/m1
    dVy1dt = (F12y + F13y)/m1
    dVx2dt = (-F12x + F23x)/m2
    dVy2dt = (-F12y + F23y)/m2
    dVx3dt = (-F13x - F23x)/m3
    dVy3dt = (-F13y - F23y)/m3
    dx1dt = X[0]
    dy1dt = X[2]
    dx2dt = X[4]
    dy2dt = X[6]
    dx3dt = X[8]
    dy3dt = X[10]
    return [dVx1dt, dVy1dt, dVx2dt, dVy2dt, dVx3dt, dVy3dt, dx1dt, dy1dt, dx2dt, dy2dt, dx3dt, dy3dt]
    

X0 = [Vx1, x1, Vy1, y1, Vx2, x2, Vy2, y2, Vx3, x3, Vy3, y3]
t = linspace(0,10000000,1000001)
X = odeint(func, X0, t)

plt.plot(X[:,1], X[:,3], "r--")
plt.show