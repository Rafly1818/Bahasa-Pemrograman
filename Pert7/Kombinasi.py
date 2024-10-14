def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n-1)

def kombinasi(n, k):
    if k > n:
        return 0
    return faktorial(n) // (faktorial (k) * faktorial(n - k))

n_input = input("Masukkan nilai n : ")
k_input = input("Masukkan nilai k (jumlah elemen yang dipilih) : ")

try:
    n = int(n_input)
    k = int(k_input)
    if n < 0 or k < 0:
        print("Masukkan bilangan bulat non-negatif.")
    else:
        hasil = kombinasi(n, k)
        print(f"Kombinasi dari {n} elemen diambil {k} sebanyak {hasil}")

except ValueError:
    print("Pastikan anda memasukkan bilangan bulat.")