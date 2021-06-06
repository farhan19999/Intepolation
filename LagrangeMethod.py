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

if __name__ =='__main__':
    x = [10, 15, 20, 22.5]
    y = [227.4, 362.78, 517.35, 602.97]
    print('velocity at t = 16 using third order polynomial', lagrangeMethod(x = 16, n =3, X = x, Y= y ))

