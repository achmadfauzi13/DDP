kendaraan = ["motor","vario","160","hijau","roda 2,"]
print(kendaraan)

kendaraan.append("Rp24.000.000")
kendaraan.append("matic")
kendaraan.insert(2,"Honda")
print("kendaraan ini saya gunakan untuk keperluan sehari-hari")
print(kendaraan)

#
menghitung = input("pilih operasi: \n 1.hitung luas persegi \n 2.hitung luas lingkaran \n 3.hitung luas segitiga \n pilihan")
match menghitung:
   case "1":
      sisi = int(input("masukan nilai sisi:"))
      luas = sisi*sisi
      print(luas)
   case "2":
      jari_jari = int(input("masukan nilai jari-jari:"))
      luas = 3,14*jari_jari*jari_jari
      print(luas)
   case "3":
      alas = int(input("masukan nilai alas:"))
      tinggi = int(input("masukan nilai tinggi:"))
      luas = 0.5*alas*tinggi
      print(luas)
   case _:
      print("salah pilih")