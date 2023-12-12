def persegi(s):
    luas = s * s
    keliling = 4 * s
    print(f"keliling persegi dengan sisi{s} adalah {keliling}")
    print(f"keliling persegi dengan sisi{s} adalah {luas}")
    
def segitiga(a,t,b,c):
    luas = 0.5*a*t
    keliling = a+b+c    
    print("luas",luas)
    print("keliling",keliling)
    
def persegipanjang(p,l):
    print("luas",p*l)
    print("keliling",2*(p+l))

def belahketupat(d1,d2,a,b,c,d):
    luas = 0.5*d1*d2
    keliling = a+b+c+d
    print("luas",luas)
    print("keliling",keliling)
    
def jajargenjang(t,a,b,c,d):
    print("luas",a*t)
    print("keliling",a+b+c+d)
    
def lingkaran(r):
    luas = 3.14*r*r
    keliling = 2*3.14*r
    print("luas",luas)
    print("keliling",keliling)
    
def trapesium(t,a,b,c,d):
    luas = (a+b)/2*t
    keliling = a+b+c+d
    print("luas",luas)
    print("keliling",keliling)