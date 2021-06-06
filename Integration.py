from sympy import * 
import LagrangeMethod as LM

v1 = [22, 25, 27, 30]
v2 = [30, 31, 35, 37]
p1 = [44, 43, 42, 40]
p2 = [40, 35, 30, 25]

x = Symbol('x') 
f = LM.lagrangeMethod(x, 3, v1, p1) 
F = integrate(f) 
print('f = ', f) 
print('F = ', F) 
F= lambdify(x, F) 
w1 = F(30)-F(25) 

f = LM.lagrangeMethod(x, 3, v2, p2) 
F = integrate(f) 
print('f =', f) 
print('F =', F) 
F= lambdify(x, F) 
w2 = F(35)-F(30)

print('total work = ', w1+w2) 