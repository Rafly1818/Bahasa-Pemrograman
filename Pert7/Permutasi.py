def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n - 1)

def permutasi(n, r):
    if n < r:
        return 0
    else:
        return faktorial(n) // faktorial(n - r)

n = int(input("Masukkan nilai n : "))
r = int(input("Masukkan nilai r : "))

print()

hasil = permutasi(n, r)
print("Hasil permutasi n dengan r adalah : ", hasil)