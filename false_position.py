# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 21:46:17 2022

@author: Mugdho
"""

import math
import numpy as np
import sys
from xlwt import Workbook
print("f(x)= (667.8/x)*(1-e^-0.146843x)")
a = int(input("Enter 1st Guess:  "))
b = int(input("Enter 2nd Guess:  "))
fxa = (667.38/a)*(1-math.exp(-0.146843*a))-40
fxb = (667.38/b)*(1-math.exp(-0.146843*b))-40
if fxa*fxb>0:
    print("wrong inital value .......",fxa*fxb,"....value must be less than 0,plz try again")
    sys.exit()

elif fxa*fxb<0:
     err = float(input("enter the error value :"))
     ite = int(input("enter the iteration :"))
     x_a = np.zeros([ite])#making array 
     x_b = np.zeros([ite])#making array 
     x_c = np.zeros([ite])#making array 
     f_a = np.zeros([ite])
     f_b = np.zeros([ite])
     f_c = np.zeros([ite])
     real_err = np.zeros([ite])
     itern = np.zeros([ite])
     x_a[0]= a
     x_b[0]= b
     f_a[0]=fxa
     f_b[0]=fxb
     for i in range(ite):
         itern[i]=i+1
         
         f_a[i] = (667.38/x_a[i])*(1-math.exp(-0.146843*x_a[i]))-40
         f_b[i] = (667.38/x_b[i])*(1-math.exp(-0.146843*x_b[i]))-40
         
         x_c[i]= x_b[i] - (x_a[i]-x_b[i]) * f_b[i]/( f_a[i] - f_b[i])
         f_c[i] = (667.38/x_c[i])*(1-math.exp(-0.146843*x_c[i]))-40
         if i>0:
             real_err[i]=((x_c[i]-x_c[i-1])/x_c[i])*100 # error estimation = ({xc[new]-xc(old)}/xc[new])x100
         
         if all ([i>0, abs(real_err[i])<err]):
             break 
         elif f_c[i]==0:
             break
    
         if i==ite-1:
             break
         if all ([f_c[i]>0, f_a[i]>0]):
             x_a[i+1]=x_c[i]
             x_b[i+1]=x_b[i]
         elif all ([f_c[i]>0, f_b[i]>0]):
             x_b[i+1]=x_c[i]
             x_a[i+1]=x_a[i]
         elif all ([f_c[i]<0, f_a[i]<0]):
             x_a[i+1]=x_c[i]
             x_b[i+1]=x_b[i]
         elif all ([f_c[i]<0, f_b[i]<0]):
             x_b[i+1]=x_c[i]
             x_a[i+1]=x_a[i]
         #creating excel
         wb = Workbook()
         sheet1 = wb.add_sheet('Sheet 1')
         num_of_iter=i
         
         #writing on excel
         sheet1.write(0,4,"False Position")
         sheet1.write(1,0,'Number of iteration') # row, column , value
         sheet1.write(1,1,'x_a')
         sheet1.write(1,2,'x_b')
         sheet1.write(1,3,'f(a)')
         sheet1.write(1,4,'f(b)')
         sheet1.write(1,5,'x_c')
         sheet1.write(1,6,'f(c)')
         sheet1.write(1,7,'Relative error')
         
         #writing values on excel    
         for n in range(num_of_iter+1):
             
             sheet1.write(n+2,0,itern[n])
             sheet1.write(n+2,1,x_a[n])
             sheet1.write(n+2,2,x_b[n])
             sheet1.write(n+2,3,f_a[n])
             sheet1.write(n+2,4,f_b[n])
             sheet1.write(n+2,5,x_c[n])
             sheet1.write(n+2,6,f_c[n])
             sheet1.write(n+2,7,real_err[n])
         
         sheet1.write(n+4,2,'The')
         sheet1.write(n+4,3,'root')
         sheet1.write(n+4,4,'is')
         sheet1.write(n+4,5,x_c[i])
         
         #save the excel file
         wb.save('false position example.xls')
         
     print([np.transpose(x_a)],[np.transpose(x_b)])
     print ("the root is",x_c[i])