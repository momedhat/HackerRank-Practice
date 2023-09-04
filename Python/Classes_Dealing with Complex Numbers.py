"""
("Classes: Dealing with Complex Numbers"), you are tasked with creating a class for complex numbers and implementing various operations on them. The scenario typically includes the following:

Complex numbers are represented as a + bi, where a is the real part, and b is the imaginary part.
Your objective is to implement a class, often named Complex, that supports operations such as addition, subtraction, multiplication, and division of complex numbers.
Task:
You need to implement the Complex class with methods for performing the following operations:

Addition of two complex numbers: (a + bi) + (c + di) = (a + c) + (b + d)i
Subtraction of two complex numbers: (a + bi) - (c + di) = (a - c) + (b - d)i
Multiplication of two complex numbers: (a + bi) * (c + di) = (ac - bd) + (ad + bc)i
Division of two complex numbers: (a + bi) / (c + di) = ((ac + bd) / (c^2 + d^2)) + ((bc - ad) / (c^2 + d^2))i
"""

### Solution ###

import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, no):
        real_num = self.real + no.real
        imag_num = self.imaginary + no.imaginary
        return Complex(real_num,imag_num)
    
    def __sub__(self, no):
        real_num = self.real - no.real
        imag_num = self.imaginary - no.imaginary
        return Complex(real_num,imag_num)
        
    def __mul__(self, no):
        real_num = self.real*no.real - self.imaginary*no.imaginary
        imag_num = self.real*no.imaginary + self.imaginary*no.real
        return Complex(real_num,imag_num)

    def __truediv__(self, no):
        conjugate = Complex(no.real, -no.imaginary)
        denominator = float(no.real**2 + no.imaginary**2)
        numerator = self * conjugate
        
        real_num = numerator.real / denominator
        imag_num = numerator.imaginary / denominator
        return Complex(real_num,imag_num)

    def mod(self):
        real_num = (self.real**2 + self.imaginary**2)**0.5
        return Complex(real_num,0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
