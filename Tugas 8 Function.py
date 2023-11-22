
def profile(nama,alamat,gader,umur,hoby):
    print("nama : " , nama)
    print("alamt : " , alamat)
    print("jeniskelamin : " , gader)
    print("usia : " , umur)
    print("hobi : " , hoby)
profile("achmad fauzi","jln.gbhn des.bojong nangka","laki-laki","19 thn","bulutangkis")

def nilaiUTs (nilai):
    if  nilai < 60:
        print ("gagal")
    elif nilai <=61 and nilai <=70:
        print ("baik")
    elif nilai <=71 and nilai <=80:
        print ("sangat baik")
    elif nilai <=81 and nilai <=100:
        print("istimewa")
    else : 
        print ("tidak ada")
nilaiUTs(60)

def nilai_Uts_ganjil(nilai):
    for i in range (nilai):
        if i % 2 != 0 :
            print(i)
nilai_Uts_ganjil(100)
