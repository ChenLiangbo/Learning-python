# -*- coding: utf-8 -*-
from sympy import *

init_printing()
x,t,z,nu = symbols('x,t,z,nu')
# init_session()

# 微分
# dsin = diff(sin(x)*exp(x),x,2)
# print('dsin = ')
# pprint(dsin)

#积分
# isin = integrate(exp(x)*sin(x)+exp(x)*cos(x),x)
# print('isin = ')
# pprint(isin)
#定积分
# isin2 = integrate(sin(x**2),(x,-oo,oo)) 
# print ('isin2 = ')
# pprint(isin2)

#极限
# lsinx = limit(sin(x)/x,x,0)
# print ('lsinx = ',lsinx)

#解代数方程
# roots = solve(x**2-2,x)
# print ("roots = ",)
# pprint(roots)

# #常微分方程
# y = Function('y')
# dy = dsolve(Eq(y(t).diff(t,t) - y(t),exp(t)),y(t))
# print ('dsolve = ',)
# pprint(dy)

#表达式求值,替换
# expression = sin(x) + 1
# pprint(expression.subs(x,pi/2))
# pprint(expression.subs(x,t))
# pprint(expression.subs(x,x*exp(t)))

#高级运算表达式
x,y,z = symbols('x,y,z')
expression = x**2 + x*y
srepr(expression)
pprint(expression)
# dotprint(expression)