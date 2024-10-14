def deret_2(n):
    if n == 1:
        return 2
    else:
        return 2 * n + deret_2(n - 1)


n = int(input("Masukkan nilai n untuk Studi Kasus 2: "))


hasil = deret_2(n)
print(f"Hasil deret 2+4+6+...+{2*n} adalah {hasil}")