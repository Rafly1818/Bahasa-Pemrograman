def penjumlahan(x, y):
    return x + y
    
def pengurangan(x, y):
    return x - y
    
def perkalian(x, y):
    return x * y
    
def pembagian(x, y):
    if y == 0:
        return("Error : Tidak bisa pembagian dengan angka nol.")
    else:
        return x / y


def kalkulator():
    print("Operasi bilangan \n")
    print("1. penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print()
    
    pilihan = input("Masukkan pilihan anda : ")
    print()
    
    num1 = float(input("Masukkan angka pertama : "))
    num2 = float(input("Masukkan angka kedua : "))
    
    if pilihan == '1':
        print("Hasil penjumlahan : ", penjumlahan(num1, num2))
    elif pilihan == '2':
        print("Hasil pengurangan : ", pengurangan(num1, num2))
    elif pilihan == '3':
        print("Hasil perkalian : ", perkalian(num1, num2))
    elif pilihan == '4':
        print("Hasil pembagian : ", pembagian(num1, num2))
    else:
        print("GAADAAA")
kalkulator()

print()

def celcius_ke_fahrenheit(celcius):
    return(celcius * 9/5) + 32
    
def celcius_ke_kelvin(celcius):
    return celcius + 273.15
    
def celcius_ke_reamur(celcius):
    return celcius * 4/5
    
celcius = float(input("Masukkan suhu dalam celcius : "))

faherenheit = celcius_ke_fahrenheit(celcius)
print (f"{celcius} derajat Celcius sama dengan {faherenheit} derajat Fahrenheit.")

kelvin = celcius_ke_kelvin(celcius)
print (f"{celcius} derajat Celcius sama dengan {kelvin} derajat kelvin.")

reamur = celcius_ke_reamur(celcius)
print (f"{celcius} derajat Celcius sama dengan {reamur} derajat reamur.")

print()

def konversi_nilai(angka):
    if angka >= 85:
        return "A"
    elif angka >= 70:
        return "B"
    elif angka >= 60:
        return "C"
    elif angka >= 50:
        return "D"
    else:
        return "E"

nilai_angka = float(input("Masukkan nilai anda : "))

nilai_huruf = konversi_nilai(nilai_angka)

print(f"Nilai huruf untuk nilai angka {nilai_angka} adalah {nilai_huruf}.")