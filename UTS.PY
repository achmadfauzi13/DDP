True
kelas="duabelas"
walikelas="pakrungkad"
pelajarankiller="ilmujiwa"
print(kelas,walikelas,pelajarankiller)
False
kelasdua2="duabelas"
walikelas="pakrungkad"
pelajarankiller="ilmujiwa"
print(kelas)

diag1= float(input("masukan panjang diag1 :"))
diag2= float(input("masukan panjang diag2 :"))
print("^^^^^^^^^^^^^^^^^^^^^")

sisi1= float(input("masukan panjang sisi1: "))
sisi2= float(input("masukan panjang sisi2 :"))
print("^^^^^^^^^^^^^^^^^^")

luas= 0.5 * diag1 * diag2
keliling= 2 * (sisi1+sisi2)

print(f"luas layang layang: {luas}")
print(f"keliling layang layang: {keliling}")
print("********************")

angka_1 = int(input('masukkan angka pertama : '))
option = input('pilih opsi (+,-,*,/,**): ')
angka_2 = int(input('masukkan angka kedua   : '))

opsi_plus = angka_1 + angka_2
opsi_min = angka_1 - angka_2
opsi_kali = angka_1 * angka_2
opsi_bagi = angka_1 / angka_2
opsi_pangkat= angka_1 ** angka_2

print('|||||||||||||||||||||')

if option == '+':
    print('Hasilnya adalah : ' + str(opsi_plus))
elif option == '-':
    print('Hasilnya adalah : ' + str(opsi_min))
elif option == '*':
    print('Hasilnya adalah : ' + str(opsi_kali))
elif option == '**':
    print('Hasilnya adalah : ' + str(opsi_pangkat))
elif option == '/':
    print('Hasilnya adalah : ' + str(opsi_bagi))
    print('dan jika dibulatkan, menjadi ' + str(round(opsi_bagi)))
