import math

def ileri_turev (f, x, h = 1e-1):
    df = f(x+h)-f(x)
    return df/h

def geri_turev (f, x, h = 1e-1):
    df = f(x)-f(x-h)
    return df/h 

def simetrik_turev (f, x, h = 1e-1):
    df = f(x+h)-f(x-h)
    return df/(2*h)

func = lambda x: x**2+5*x+1
funct = lambda x: 2*x+5
x0 = 3
fi = ileri_turev (func, x0)
fg = geri_turev (func, x0)
fs = simetrik_turev (func, x0)

print("x0 = 3 noktasındaki türev: f_ileri = {0}, f_geri = {1}, f_sim = {2}, => f_tam(x) = {3}".format(fi, fg, fs, funct(x0)))