# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 21:54:32 2022

@author: Mugdho
"""
#f(x)= (e^-x)-x
import numpy as np
import math
import xlwt
from xlwt import Workbook
x1 = int(input("Enter a X(i-1) Value: "))
x2= int(input("Enter another value(Xi): "))
ite=int(input("Enter eteration value: "))
tol = float(input("Enter tolerance value: "))
y = lambda x:((math.exp(- x) )-x)

fnx1 = y(x1)
fnx2 = y(x2)

x_1=np.zeros([ite])
x_2=np.zeros([ite])
f_nx1=np.zeros([ite])
f_nx2=np.zeros([ite])
rel_err=np.zeros([ite])
itern=np.zeros([ite])
x_new=np.zeros([ite])  
f_xnew = np.zeros([ite])    
x_1[0]= x1
x_2[0]=x2
 
f_nx1[0]=fnx1
f_nx2[0]=fnx2
for i in range(ite):
    
   
    f_nx1[i]=y(x_1[i])
    f_nx2[i]= y(x_2[i])
    x_new[i]=x_2[i]-(x_1[i]-x_2[i])/(f_nx1[i]-f_nx2[i])*f_nx2[i]
    f_xnew[i] = math.exp(-x_new[i]) - x_new[i]
    itern[i]= i+1
    #calculating error    
    if i>0:
        rel_err[i]=((x_new[i]-x_new[i-1])/x_new[i])*100
    if all([i>0,abs(rel_err[i]<tol)]):
        break
    elif f_xnew[i]==0:
        break
    

    if i==ite-1:
        break
    
    x_1[i+1]=x_2[i]
    x_2[i+1]=x_new[i]
    
print("The root is",x_new[i])