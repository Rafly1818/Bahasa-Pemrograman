def konversi_nilai(angka):
    if angka <= 100 and angka >= 85:
        return "A"
    elif angka <= 84 and angka >= 70:
        return "B"
    elif angka < 70 and angka >= 60:
        return "C"
    elif angka < 60 and angka >= 50:
        return "D"
    elif angka < 50 and angka >= 0:
        return "E"
    else:
        return "GAADAA"

nilai_angka = float(input("Masukkan nilai anda : "))

nilai_huruf = konversi_nilai(nilai_angka)

print(f"Nilai huruf untuk nilai angka {nilai_angka} adalah {nilai_huruf}.")

print()

def pembagian_kategori(umur):
    if umur < 5:
        return "Balita"
    elif umur >= 5 and umur < 12:
        return "Anak-anak"
    elif umur >= 12 and umur < 18:
        return "Remaja"
    elif umur >= 18 and umur < 40:
        return "Dewasa"
    elif umur >= 40 and umur < 60:
        return "Paruh Baya"
    elif umur >= 60:
        return "Lanjut Usia"

nilai_umur = int(input("Masukkan umur anda : "))

nilai_kategori = pembagian_kategori(nilai_umur)

print(f"Anda ada di kategori {nilai_kategori} dengan umur {nilai_umur} tahun.")