def faktorial(n):
    if n == 0:
        return 1
    else:
        return n *faktorial(n-1)

user_input = input("Masukkan bilangan untuk menghitung faktorial : ")
try:
    angka = int(user_input)
    if angka < 0:
        print ("Masukkan bilangan non-negatif")
    else:
        hasil = faktorial(angka)
        print (f"Faktorial dari {angka} adalah {hasil}")

except ValueError:
    print("Masukkan bilangan bulat yang valid.")