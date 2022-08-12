# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 16:19:50 2022

@author: Arif
"""

#Import libraries as necessary
import math
import numpy as np
import sys

#Take necessary input
#For bisection, two input is required to bracket the root
xl=float(input ('Enter 1st initial value: '))   #1st input
print(xl)
xu=float(input ('Enter 2nd initial value: '))   #2nd input

fxl=(667.38/xl)*(1-math.exp(-0.146843*xl))-40
fxu=(667.38/xu)*(1-math.exp(-0.146843*xu))-40

if fxl*fxu>0: # choose two real number a & b such that f(a)*f(b)<0
        print('Wrong initial input')
        sys.exit()
        
elif fxl*fxu<0:     # steps start
    
    err=float(input('Enter desired percentage relative error: '))
    ite=int(input('Enter number of iterations: '))

    x_l=np.zeros([ite]) 
    x_u=np.zeros([ite])
    x_c=np.zeros([ite])
    
    f_xl=np.zeros([ite])
    f_xu=np.zeros([ite])
    f_xc=np.zeros([ite])
    
    rel_err=np.zeros([ite])
    itern=np.zeros([ite])
    
    x_l[0]=xl
    x_u[0]=xu
    
    f_xl[0]=fxl
    f_xu[0]=fxu 
       
    for i in range(ite):
    
        itern[i]=i+1
        x_c[i]=(x_l[i]+x_u[i])/2 #bisection method root eqn
        
        f_xl[i]=(667.38/x_l[i])*(1-math.exp(-0.146843*x_l[i]))-40
        f_xu[i]=(667.38/x_u[i])*(1-math.exp(-0.146843*x_u[i]))-40
        f_xc[i]=(667.38/x_c[i])*(1-math.exp(-0.146843*x_c[i]))-40
            
        if i>0:
            rel_err[i]=((x_c[i]-x_c[i-1])/x_c[i])*100 # error estimation = ({xc[new]-xc(old)}/xc[new])x100
        
        if all ([i>0, abs(rel_err[i])<err]):
            break 
        elif f_xc[i]==0:
            break
   
        if i==ite-1:
            break
        
        if all ([f_xc[i]>0, f_xl[i]>0]):
            x_l[i+1]=x_c[i]
            x_u[i+1]=x_u[i]
        elif all ([f_xc[i]>0, f_xu[i]>0]):
            x_u[i+1]=x_c[i]
            x_l[i+1]=x_l[i]
        elif all ([f_xc[i]<0, f_xl[i]<0]):
            x_l[i+1]=x_c[i]
            x_u[i+1]=x_u[i]
        elif all ([f_xc[i]<0, f_xu[i]<0]):
            x_u[i+1]=x_c[i]
            x_l[i+1]=x_l[i]
        
    print([np.transpose(x_l)],[np.transpose(x_u)])
    print ("the root is",x_c[i])    



