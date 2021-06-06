x = [0,10,15,20,22.5,30]
y = [0,227.4,362.78,517.35,602.97,901.67]

def b_func(m,n):
    
    if m == n :
        return y[m]
    else :
        return (b_func(m,n+1)-b_func(m-1,n))/(x[m]-x[n])
    
def interpolate_func(X,n):
    
    ans = 0
    i=0
    while(i<=n):
        j = 0
        coeff = b_func(i,0)
        while(j<i):
            coeff *= (X-x[j])
            j+=1
        ans+=coeff
        i+=1
    return ans
    
if __name__ == '__main__':
    print(interpolate_func(16,3))
    