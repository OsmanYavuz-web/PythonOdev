# paket
import sympy as sp
sp.init_printing()

# x değişkeni
x = sp.Symbol('x')

# f değişkeni
f = sp.Function('f')
f = (sp.sin(x)) * sp.exp(3*x)

sp.diff(f, x)

# Ekrana yazdırma
print("Çıktı: ", sp.diff(f,x))