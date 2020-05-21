# paket
import sympy as sp
sp.init_printing()

# x değişkeni
x = sp.Symbol('x')

# f değişkeni
f = sp.Function('f')
f = x*sp.sin(x)

# g değişkeni
g = sp.integrate(f, (x ,0, 4))

# Ekrana yazdırma
print(g)
print("Çıktı: ", g.evalf())