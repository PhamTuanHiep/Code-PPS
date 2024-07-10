import array as arr
import math as mt

X= arr.array('d',[2.651,2.778,2.905,3.032,3.159,3.286,3.413,3.54,3.667,3.794,3.921,4.048,4.175,4.302])
Y= arr.array('d',[2.93027,2.8834,2.64288,2.21651,1.62532,0.90269,0.09245,-0.75382,-1.5802,-2.33018,-2.95068,-3.339581,-3.63035,-3.63246])
n=len(X)-1
m=len(Y)-1
print (m)
print (n)

def P(y):
    P=0
    for i in range(n+1):
        L=1
        for j in range(n+1):
            if(i==j):
                continue
            L=L*(y-Y[j])/(Y[i]-Y[j])
        # arr_L.append(M1/M2)
        P=P+X[i]*L
    # print(arr_L)
    return P
y=-3
print("P(",y,") = ",P(y))
