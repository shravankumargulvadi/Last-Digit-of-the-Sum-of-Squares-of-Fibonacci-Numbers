
# coding: utf-8

# In[3]:


import numpy as np
def LD_sum_fib(j):
    
    
    a=np.random.randint(1, 10000, 3)
    a[0]=0
    sum=0
    if j>0:
        a[1]=1
        sum=1
        i=indexfinder(10)
        if j<=i:
            for j in range(2, j+1):
                a[2]=(a[0]+a[1])%10
                a[0]=a[1]
                a[1]=a[2]
                sum=sum+a[2]*a[2]
        if j>i:
            sum=sumfinder(i)
            sum=int(j/(i))*sum+sumfinder(j%(i))
        
        
    return sum%10
def sumfinder(m):
    a=np.random.randint(1, 10000, 3)
    a[0]=0
    sum=0
    if m>0:
    
        a[1]=1
        sum=1
        for k in range(2, m+1):
            a[2]=(a[0]+a[1])%10
            a[0]=a[1]
            a[1]=a[2]
            sum=sum+a[2]*a[2]
    #print(sum)            
    return sum%10
def indexfinder(m):
    i=1
    a=0
    f=np.random.randint(1, 100, 2)
    f[0]=0
    f[1]=1
    while a!=1:
        f=np.float64(f)
        z=f[1]
        f[1]=f[0]+f[1]
        f[0]=z
        f[0]=f[0]%m
        f[1]=f[1]%m
        
        a=(f[0])+(f[1])
        a=np.float64(a)
        
        
        if a==1:
            #print('completed index \n')
            #print(i+1)
            return i+1
        else:
            i=i+1
            #print(i)
if __name__ == '__main__':
    input_n = int(input())
    print(LD_sum_fib(input_n))
        
    

