while True:
  # Kullanıcı veri girişi
  daire_yari_cap = input("Yarıçapı Girin: ") 
 
  # Dairenin çevresini hesaplama
  daire_cevre = (2 * 3.14 * float(daire_yari_cap))
  
  # Dairenin alanını hesaplama
  daire_alan = 3.14 * float(daire_yari_cap) * float(daire_yari_cap)

  # Ekrana yazdırma
  print("Dairenin Alanı: ", daire_alan )
  print("Dairenin Çevresi: ", daire_cevre)
  print("\n")