import math

def penjumlahan(b1,b2):
    hasil = b1 + b2
    print(b1,"+", b2, "=" ,hasil)
    
def pengurangan(b1,b2):
    hasil = b1 - b2
    print(b1,"-", b2,"=",hasil)

def perkalian(b1,b2):
    hasil = b1 * b2
    print(b1,"*",b2, "=", hasil)
    
def pembagian(b1,b2):
    hasil = b1 / b2
    print(b1, "/", b2, "=", hasil)
    
def pangkat(b1,b2):
    hasil = math.pow(b1,b2)
    print("hasil-pangkat", b1, "^", b2, "hasil", hasil)
    
def akar(b1):
    hasil = math.sqrt(b1)
    print("hasil-akar", b1, "=", hasil)
    
def log(b1):
    hasil = math.log(b1)
    print("hasil-lagoritma", b1, "=", hasil)
    
def sin(nilai):
    hasil = math.sin(nilai)
    print("hasil sin dari", nilai, "=", hasil)
    
def cos(nilai):
    hasil = math.cos(nilai)
    print("hasil sin dari", nilai, "=", hasil)
    
def tan(nilai):
    hasil = math.tan(nilai)
    print("hasil tan dari", nilai, "=", hasil)