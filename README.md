## ニュートン法
```math
\begin{aligned}
f'(x_1)&=\frac{\Delta y}{\Delta x} \\
&=\frac{f(x_1)}{x_1 - x_2} \\
\Leftrightarrow x_1-x_2&=\frac{f(x_1)}{f'(x_1)} \\
\therefore x_2 &=x_1 - \frac{f(x_1)}{f'(x_1)}
\end{aligned}
```

同様の手順を用いてx3についてもx2から算出することができます

```math
\begin{aligned}
x_3 &=x_2 - \frac{f(x_2)}{f'(x_2)}
\end{aligned}
```

つまり、今ニュートン法をn回行って算出したx座標xnに対してニュートン法を適応して算出されるx座標xn+1には次のような関係式が成り立ちます

```math:ニュートン法
\begin{aligned}
x_{n+1} &=x_n - \frac{f(x_n)}{f'(x_n)}
\end{aligned}
```# math
