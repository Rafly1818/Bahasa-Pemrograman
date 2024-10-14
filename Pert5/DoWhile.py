print ("Tugas Bahasa Pemrograman\n")
 
#Buatlah Program Untuk Menampilkan Output Berikut:
#30-16, 1-15
print("===================================================")
print ("Nomor 1\n")
for i in range(30, 15, -1):
    print(i, end=" ")
for i in range(1, 16):
    print(i, end=" ")
    
print ("\n")

#Buatlah Program Untuk Menampilkan Sederetan Angka Genap Dan Ganjil Beserta Jumlahnya
print("===================================================")
print ("Nomor 2\n")

angka = int(input("Masukkan Batas Angka Ganjil : "))
jumlah1 = 0
jumlah2 = 0
for i in range(1, angka + 1):
    if i % 2 != 0:
        print(i, end=" ")
        jumlah1 += i
    if i == angka:
        print("=", jumlah1, "Total Angka Ganjil")

print() 
 
angka = int(input("Masukkan Batas Angka Ganjil : "))       
for i in range(1, angka + 1):
    if i % 2 == 0:
        print(i, end=" ")
        jumlah2 += i
    if i == angka:
        print("=", jumlah2, "Total Angka Genap")
        
print ("\n")

#Buatlah Program Untuk Menampilkan Output Berikut Dengan Menggunakan Konsep Perulangan Do-While:
print("===================================================")
print("Nomor 3\n")


angka = int(input("Masukkan Angka : ")) 
p = 1
while p <= angka/2:
    print (p)
    p += 1
while p <= angka:
    print (p, end=" ") 
    p += 1