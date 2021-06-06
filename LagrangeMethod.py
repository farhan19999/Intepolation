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
