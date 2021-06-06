def l_func(n, i, x, X):
    j = 0
    ans = 1
    while(j<=n):
        if(j != i):
            ans *= (x-X[j])/(X[i]-X[j])
        j+=1
    return  ans

def lagrangeMethod(x, n, X, Y):
    i = 0
    ans = 0
    while(i<=n):
        ans += l_func(n, i, x, X)*Y[i]
        #print('L(',i,') = ',l_func(n,i,x,X))
        i+=1
    return ans

if __name__=='__main__':
    v1 = [22, 25, 27, 30]
    v2 = [30, 31, 35, 37]
    p1 = [44, 43, 42, 40]
    p2 = [40, 35, 30, 25]
    print('Pressure at V = 28 m^3 = ', lagrangeMethod(28, 3, v1, p1))
    print('Pressure at V = 32 m^3 = ', lagrangeMethod(32, 3, v2, p2))
    
    pol2 = lagrangeMethod(28, 2, v1[1:4], p1[1:4])
    pol3 = lagrangeMethod(28, 3, v1, p1)
    error = 100*abs(pol3-pol2)/pol3
    print('absolute approximate relative error of process 1 : ',error)
    
    pol2 = lagrangeMethod(32, 2, v2[:3], p2[:3])
    pol3 = lagrangeMethod(32, 3, v2, p2)
    error = 100*abs(pol3-pol2)/pol3
    print('absolute approximate relative error of process 2 : ',error)