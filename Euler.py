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
# オイラー法の変数y
y = np.zeros(len(t))
y[0] = y0
# 実際の関数
y_exact = np.exp(t)

for i in range(len(t) - 1):
  y[i+1] =  yt + dt *f(t[i], yt)
  yt = y[i + 1]

plt.scatter(t, y, color='orange', label="Euler")
plt.plot(t, y_exact, label="function")
plt.legend()