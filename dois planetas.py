import matplotlib.pyplot as plt
from scipy.integrate import odeint
from math import sqrt
from numpy import linspace

x2 = 0
y2 = 0
x3 = 500
y3 = 200
G = 6.67428*(10**-11)
m = 10*6400000**2/G

def func(X,t):
    x = X[0]
    y = X[2]
    dx = x-x2
    dy = y-y2
    dxdt = X[1]
    dVxdt = -(G*m*dx)/((dx**2+dy**2)*(sqrt(dx**2+dy**2)))
    dydt = X[3]
    dVydt = -(G*m*dy)/((dx**2+dy**2)*(sqrt(dx**2+dy**2)))
    return [dxdt, dVxdt, dydt, dVydt]

x = 0
Vx = 8000
y = 6400000
Vy = 0
X0 = [x, Vx, y, Vy]
t = linspace(0,10000,10001)
X = odeint(func, X0, t)
#print(X[0])
plt.plot(X[:,0], X[:,2], "r--",  label="Vx")
#plt.plot(t, X[2], "r",  label="Vx")

#plt.axis(0, t(max), 0, Vx(max))
#plt.plot(t, X[2], "r",  label="Vy'")
#plt.axis(0, t(max), 0, Vy(max))
plt.show    