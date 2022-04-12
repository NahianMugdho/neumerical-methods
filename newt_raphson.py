# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 13:08:50 2022

@author: Mugdho
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 12:58:28 2022

@author: Mugdho
"""

#f(x)= (e^-x)-x


import numpy as np
import math
import xlwt
from xlwt import Workbook
a = int(input("Enter a Value: "))
ite=int(input("Enter eteration value: "))
tol = float(input("Enter tolerance value: "))
y = lambda x:((math.exp(- x) )-x)
dy = lambda x :((-(math.exp(- x) ))-x)

x_a=np.zeros([ite])
x_new=np.zeros([ite])


f_a=np.zeros([ite])
f_xnew=np.zeros([ite])


rel_err=np.zeros([ite])
itern=np.zeros([ite])
   
    
x_a[0]= a
 
f_a[0]=y(a)
f_xnew[0]=dy(a)
for i in range(ite):
    itern[i]= i+1
   
    f_a[i]=y(i)
    f_xnew[i]= dy(i)
    x_new[i]=x_a[i]-((f_a[i])/(f_xnew[i])) 
    #calculating error    
    if i>0:
        rel_err[i]=((x_new[i]-x_new[i-1])/x_new[i])*100
    if all([i>0,abs(rel_err[i]<tol)]):
        break
    elif f_xnew[i]==0:
        break

    if i==ite-1:
        break
    
    x_a[i+1]=x_new[i]

wb = Workbook()




sheet= wb.add_sheet("Newt_raphson")
#font/bold/colour/font size
header_font = xlwt.Font()

header_font.name = 'Arial'

header_font.bold = True
header_font.colour_index = 4
header_font.height = 500
header_style = xlwt.XFStyle()
header_style.font = header_font

#borders
# Thin solid line: 1, small thick solid line: 2, thin dotted line: 3, medium and thin dotted line: 4, large thick solid line: 5, double line: 6, thin dotted line: 7
# Big and thick dotted line: 8, thin dotted line: 9, thick dotted line: 10, thin double dotted line: 11, thick double dotted line: 12, oblique dotted line: 13
borders = xlwt.Borders()
borders.left = 8
borders.right = 10
borders.top = 1
borders.bottom = 4
header_style.borders = borders





ele_font = xlwt.Font()
ele_font.name = 'Arial'
ele_font.bold = True
ele_font.colour_index = 2
ele_font.height = 200
ele_style = xlwt.XFStyle()
ele_style.font = ele_font


num_of_iter = i
sheet.write(0,7,"Newton Raphson Method",header_style)

sheet.write(1,0,"No of Iteration",ele_style)
sheet.write(1,1,"Guess = a",ele_style)
sheet.write(1,2,"f(a)",ele_style)
sheet.write(1,3,"f'(a)",ele_style)
sheet.write(1,4,"Xnew",ele_style)

#column Width
sheet.col(7).width = 30032
sheet.col(0).width = 10000

for n in range( num_of_iter+1):
    sheet.write(n+2,0,itern[n])
    sheet.write(n+2,1,x_a[n])
    sheet.write(n+2,2,f_a[n])
    sheet.write(n+2,3,f_xnew[n])
    sheet.write(n+2,4,x_new[i])


sheet.write(n+6,2,'The')
sheet.write(n+6,3,'root')
sheet.write(n+6,4,'is')
sheet.write(n+6,5,x_new[i])    
    
print("The root is",x_new[i])
wb.save('newt.xls')                         