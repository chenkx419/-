# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cmath

def solve_quadratic_equation(a, b, c):
    # 计算判别式
    discriminant = (b**2) - (4*a*c)

    # 计算解
    if discriminant >= 0:
        # 实根
        root1 = (-b + discriminant**0.5) / (2*a)
        root2 = (-b - discriminant**0.5) / (2*a)
    else:
        # 复根
        real_part = -b / (2*a)
        imaginary_part = cmath.sqrt(abs(discriminant)) / (2*a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)

    return root1, root2

# 获取用户输入的a、b、c值
a = float(input("请输入a的值："))
b = float(input("请输入b的值："))
c = float(input("请输入c的值："))

# 调用函数求解一元二次方程
root1, root2 = solve_quadratic_equation(a, b, c)

# 打印解
print("解为:")
print("x1 =", root1)
print("x2 =", root2)
