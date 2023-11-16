namakendaraan = input("nama kendaraan :")
jenisbensinn= input("jenis bensin :")
kotayangdituju= input("kota tujuan :")

if jenisbensinn == "pertalite":
    harga_perliter = 10000
    jaraktempuh = 12
elif jenisbensinn == "pertamax":
    harga_perliter = 14000
    jaraktempuh = 13
elif jenisbensinn == "pertamax turbo":
    harga_perliter = 17000
    jaraktempuh =13.5

if kotayangdituju == "jakarta":
    jarak_kota = 20
elif kotayangdituju == "bekasi":
    jarak_kota = 35.7
elif kotayangdituju == "depok":
    jarak_kota = 5
elif kotayangdituju == "tanggerang":
    jarak_kota = 99
elif kotayangdituju == "bogor" :
    jarak_kota = 120.6

pemakaian_bensin= jarak_kota/ jaraktempuh
total_harga= pemakaian_bensin * harga_perliter

print("namakendaraan",namakendaraan)
print("jenisbensin",jenisbensinn)
print("kota yang di tuju",kotayangdituju)
print("pemakaian bensin",pemakaian_bensin,"liter")
print("total harga", total_harga, "rupiah")

# Input Nama Pembeli
nama_pembeli = input("Masukkan Nama Pembeli: ")
# Input No Hp Pembeli
no_hp_pembeli = input("Masukkan No Hp Pembeli: ")
# Input Pesan Menu (makanan atau minuman)
pesan_menu = input("Pesan Menu Apa? (makanan atau minuman): ")

if pesan_menu == "makanan":
    print("Menu Makanan:")
    print("1. Nasi Goreng - Rp. 15,000")
    print("2. Mie Goreng - Rp. 12,000")
    print("3. Ayam Geprek - Rp. 18,000")
    pesanan = input("Masukkan pesanan (e.g., Nasi Goreng): ")
    jumlah_pesanan = int(input("Masukkan Jumlah Pesanan: "))

    if pesanan == "Nasi Goreng":
        harga_makanan = 15000
    elif pesanan == "Mie Goreng":
        harga_makanan = 12000
    elif pesanan == "Ayam Geprek":
        harga_makanan = 18000

    total_harga = harga_makanan * jumlah_pesanan
else:
    print("Menu Minuman:")
    print("1. Aneka Jus - Rp. 15,000")
    print("2. Soft Drink - Rp. 10,000")
    print("3. Sweet Ice Tea - Rp. 5,000")
    pesanan = input("Masukkan pesanan (e.g., Aneka Jus): ")
    jumlah_pesanan = int(input("Masukkan Jumlah Pesanan: "))

    if pesanan == "Aneka Jus":
        harga_minuman = 15000
    elif pesanan == "Soft Drink":
        harga_minuman = 10000
    elif pesanan == "Sweet Ice Tea":
        harga_minuman = 5000

    total_harga = harga_minuman * jumlah_pesanan

# Output Informasi
print("Nama Pembeli:", nama_pembeli)
print("No Hp Pembeli:", no_hp_pembeli)
print("Menu yang di Pesan:", pesanan)
print("Jumlah pesanan:", jumlah_pesanan)
print("Harga yang harus di bayarkan:", total_harga, "rupiah")

#STTNF
for i in range(1, 21):
    if i % 3 == 0:
        print("STT Nurul Fikri")
    else:
        print(i)