#------------| Pyabhata/पायभटः (pybht) |------------#

import math

#---------------| Easter Egg |---------------#
# Honor to Aryabhata who discovered zero [0] #

def shunya(var=None):
    return 0

def zero(var=None):
    return 0

#---------------| [] |---------------#

def pi(digits=10):
    a = 1.0
    b = 1.0 / math.sqrt(2)
    t = 0.25
    p = 1.0
    
    for _ in range(digits):
        a_next = (a + b) / 2
        b = math.sqrt(a * b)
        t -= p * (a - a_next) ** 2
        a = a_next
        p *= 2
    pi_approx = (a + b) ** 2 / (4 * t)
    return round(pi_approx, digits)

def e(digits=10):
    fact = 1
    e_approx = 2
    
    for i in range(2, digits + 2):
        fact *= i
        e_approx += 1 / fact
    
    return round(e_approx, digits)

#---------------| Arithmetic Functions |---------------#

def add(var1, var2):
    return var1 + var2

def sub(var1, var2):
    return var1 - var2

def mult(var1, var2):
    return var1 * var2

def divide(var1, var2):
    return var1 / var2

def sqrt(var):
    return (var ** (1/2))

def curt(var):
    return (var ** (1/3))

def root(var1, var2):
    return (var1 ** (1/var2))

def sq(var):
    return var ** 2

def cu(var):
    return var ** 3

def expo(var1, var2):
    return var1 ** var2

#---------------| Trigonometry Functions |---------------#

def sin(angle):
    return math.sin(math.radians(angle))

def cos(angle):
    return math.cos(math.radians(angle))

def tan(angle):
    return math.tan(math.radians(angle))

def asin(value):
    return math.degrees(math.asin(value))

def acos(value):
    return math.degrees(math.acos(value))

def atan(value):
    return math.degrees(math.atan(value))

#---------------| Calculus Functions |---------------#

def derivative(func, x, h=1e-7):
    return (func(x + h) - func(x)) / h

def integral(func, a, b, n=1000):
    h = (b - a) / n
    result = 0.5 * (func(a) + func(b))
    for i in range(1, n):
        result += func(a + i * h)
    result *= h
    return result
