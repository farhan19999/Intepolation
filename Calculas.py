
from sympy import *
import LagrangeMethod as LM

if __name__ == '__main__':
    x = Symbol('x')
    vx = [10, 15, 20, 22.5]
    vy = [227.4, 362.78, 517.35, 602.97]
    f = LM.lagrangeMethod(x, 3, vx, vy)
    f_prime = f.diff(x)
    print(f)
    print(f_prime)
    f_prime = lambdify(x,f_prime)
    print(f_prime(16))
    F = f.integrate(x)
    print(F)
    F = lambdify(x, F)
    print(F(16)-F(11))