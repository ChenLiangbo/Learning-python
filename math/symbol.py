# -*- coding: utf-8 -*-
from sympy import *

x = Symbol('x')
expand(exp(I*x), complex=True)
tmp = series(exp(I*x), x, 0, 10)  #泰勒展开
print ("tmp = ")
pprint(tmp)
# print ("tmp re = ")
# pprint(re(tmp))
# print ("cos = ")
# pprint( series( cos(x), x, 0, 10) )
# print ("tmp im = ")
# pprint(im(tmp))
# print ("sin = ")
# pprint(series(sin(x), x, 0, 10))

sinsym = integrate(x*sin(x), x)    #计算符号积分
print ("sinsym = ")
pprint(sinsym)

x, y, r = symbols('x,y,r')  #创建多个符号
2 * integrate(sqrt(r*r-x**2), (x, -r, r))  #圆的面积
print("-"*80)
r = symbols('r', positive=True)
circle_area = 2 * integrate(sqrt(r**2-x**2), (x, -r, r))
circle_area = circle_area.subs(r, sqrt(r**2-x**2))  #subs可以进行公式替换
# expression.subs(x, y) : 将算式中的x替换成y
# expression.subs({x:y,u:v}) : 使用字典进行多次替换 顺序执行
# expression.subs([(x,y),(u,v)]) : 使用列表进行多次替换 顺序执行
body = integrate(circle_area, (x, -r, r))
# pprint(body)

a = Rational(1,2)  #表示分数1/2
pprint(pi.evalf())

# apart(expr, x) #局部代数式子展开
 # together(1/x + 1/y + 1/z) #代数式子的合并 是apart的逆运算
 # latex(exp(I*x)) #转换为LaTeX公式复制输入