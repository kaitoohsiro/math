import numpy as np
import matplotlib.pyplot as plt
 
# f(t,y)
def f(t, y):
  return np.exp(t)

# 初期条件
y0 = 1
yt = y0
dt = 0.1
# 区間
t = np.arange(0, 1.1, dt)
# ルンゲ・クッタ法の変数
y = np.zeros(len(t))
y[0] = y0
# 実際の関数
y_exact = np.exp(t)
for i in range(len(t) - 1):
  k1 = dt * f(t[i], y[i])
  k2 = dt * f(t[i] + dt/2, y[i] + k1/2)
  k3 = dt * f(t[i] + dt/2, y[i] + k2/2)
  k4 = dt * f(t[i] + dt, y[i] + k3)
  y[i+1] =  y[i] + (1/6) * (k1 + 2*k2 + 2*k3 + k4)

plt.scatter(t, y, color='orange', label="Euler")
plt.plot(t, y_exact, label="function")
plt.legend()