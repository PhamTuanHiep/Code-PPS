import pandas as pd
import numpy as np
import statsmodels.api as sm
import math as mt
# xlsxFile = pd.read_excel('../Data/data GK 20231 PPS.xlsx',sheet_name="Sheet1", header=0)
xlsxFile = pd.read_excel('../Data/NS_Cachdeu_Sin.xlsx',sheet_name="Sheet1", header=0)
xlsxFile.rename(str.lower, axis='columns',inplace=1)

# print(xlsxFile)
y=xlsxFile['y']


def SP(y):
    n=len(y)
    Y = np.zeros((n , n))
    Y[:,0]=y
    for j in range(1,n): #cot
        for i in range(0,n-j):#hang
            Y[i,j]=Y[i+1,j-1]-Y[i,j-1]
    return Y

# print(SP(y))
# dY = np.zeros((n , n))

dY=SP(y)
n=len(y)

with open("file.txt", "w") as file:
    # Ghi dữ liệu vào file
    for i in range(0,n):
        for j in range(0,n):
            file.write(str(dY[i,j])+"\t")
        file.write("\n")





