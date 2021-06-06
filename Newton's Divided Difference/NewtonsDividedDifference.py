def b_func(m, n, X, Y):
    
    if m == n :
        return Y[m]
    else :
        return (b_func(m,n+1,X, Y)-b_func(m-1,n, X, Y))/(X[m]-X[n])
    

def interpolate_func(x, n, X, Y):
    
    ans = 0
    i=0
    while(i<=n):
        j = 0
        coeff = b_func(i,0, X, Y)
        while(j<i):
            coeff *= (x-X[j])
            j+=1
        ans+=coeff
        i+=1
    return ans
    
