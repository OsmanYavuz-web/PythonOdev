# paket
import math
import sympy as sp
sp.init_printing()

# fonksiyon
def f(deger):
  
  # x değişkeni
  x = sp.Symbol('x')

  # f değişkeni
  f = sp.Function('f')
  f = x**2 + 5 * x + 1

  # sonuç
  sonuc = f.subs(x, deger)

  # Ekrana yazdırma
  print("Sonuç: ", sonuc)
  print("Kök:", math.sqrt(sonuc))

# Fonksiyon kullanımı
f(4)