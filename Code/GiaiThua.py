def GiaiThua(n):
    T=1
    if(n==0):
        return 1
    for i in range(1,n+1):
        T=T*i
    return T
# print(GiaiThua(4))