import math  # Untuk menghitung nilai phi
import os

def cls():
    """Membersihkan layar konsol."""
    os.system('cls' if os.name == 'nt' else 'clear')

def hitung_luas_persegi(sisi):
    """Menghitung luas persegi."""
    return sisi * sisi

def hitung_keliling_persegi(sisi):
    """Menghitung keliling persegi."""
    return 4 * sisi
    
def hitung_luas_persegi_panjang(panjang, lebar):
    """Menghitung luas persegi panjang."""
    return panjang * lebar 
    
def hitung_keliling_persegi_panjang(panjang, lebar):
    """Menghitung keliling persegi panjang."""
    return 2 * (panjang + lebar)

def hitung_luas_segitiga(alas, tinggi):
    """Menghitung luas segitiga."""
    return 0.5 * alas * tinggi 
    
def hitung_keliling_segitiga(alas, sisi1, sisi2):
    """Menghitung keliling segitiga."""
    return alas + sisi1 + sisi2

def hitung_luas_lingkaran(jari_jari):
    """Menghitung luas lingkaran."""
    return math.pi * jari_jari * jari_jari
    
def hitung_keliling_lingkaran(jari_jari):
    """Menghitung keliling lingkaran."""
    return 2 * math.pi * jari_jari

def menu():
    """Menampilkan menu dan mengembalikan pilihan pengguna."""
    cls()  # Bersihkan layar sebelum menampilkan menu
    print("Pilih bangun datar yang tersedia")
    print()
    print("1. Persegi (Luas & Keliling)")
    print("2. Persegi Panjang (Luas & Keliling)")
    print("3. Segitiga (Luas & Keliling)")
    print("4. Lingkaran (Luas & Keliling)")
    print("5. Keluar")
    print()
    pilihan = int(input("Masukkan pilihan Anda: "))
    return pilihan
    
def tampilkan_hasil_luas_keliling(pilihan):
    """Menampilkan hasil perhitungan berdasarkan pilihan pengguna."""
    if pilihan == 1:
        cls()
        print("Rumus Luas & Keliling Persegi")
        print()
        print("Rumus Luas Persegi (Sisi x Sisi)")
        print("Rumus Keliling Persegi (4 x Sisi)")
        print()
        print("=====================================")
        sisi = float(input("Masukkan panjang sisi: "))
        cls()
        print("Hasil Perhitungan")
        print()
        luas = hitung_luas_persegi(sisi)
        keliling = hitung_keliling_persegi(sisi)
        print("Luas persegi:", luas)
        print("Keliling persegi:", keliling)
        print()
        
    elif pilihan == 2:
        cls()
        print("Rumus Luas & Keliling Persegi Panjang")
        print()
        print("Rumus Luas Persegi Panjang (Panjang x Lebar)")
        print("Rumus Keliling Persegi Panjang (2 x (Panjang + Lebar))")
        print()
        print("=====================================")
        panjang = float(input("Masukkan panjang: "))
        lebar = float(input("Masukkan lebar: "))
        cls()
        print("Hasil Perhitungan")
        print()
        luas = hitung_luas_persegi_panjang(panjang, lebar)
        keliling = hitung_keliling_persegi_panjang(panjang, lebar)
        print("Luas persegi panjang:", luas)
        print("Keliling persegi panjang:", keliling)
        print()
        
    elif pilihan == 3:
        cls()
        print("Rumus Luas & Keliling Segitiga")
        print()
        print("Rumus Luas Segitiga (0.5 * alas * tinggi)")
        print("Rumus Keliling Segitiga (Alas + Sisi(1) + Sisi(2))")
        print()
        print("=====================================")
        alas = float(input("Masukkan panjang alas: "))
        tinggi = float(input("Masukkan tinggi: "))
        sisi1 = float(input("Masukkan panjang sisi 1: "))
        sisi2 = float(input("Masukkan panjang sisi 2: "))
        cls()
        print("Hasil Perhitungan")
        print()
        luas = hitung_luas_segitiga(alas, tinggi)
        keliling = hitung_keliling_segitiga(alas, sisi1, sisi2)
        print("Luas segitiga:", luas)
        print("Keliling segitiga:", keliling)
        print()
        
    elif pilihan == 4:
        cls()
        print("Rumus Luas & Keliling Lingkaran")
        print()
        print("Rumus Luas Lingkaran (phi x Jari-Jari x Jari-Jari)")
        print("Rumus Keliling Lingkaran (2 x phi x Jari-Jari)")
        print()
        print("=====================================")
        jari_jari = float(input("Masukkan jari-jari: "))
        cls()
        print("Hasil Perhitungan")
        print()
        luas = hitung_luas_lingkaran(jari_jari)
        keliling = hitung_keliling_lingkaran(jari_jari)
        print("Luas lingkaran:", luas)
        print("Keliling lingkaran:", keliling)
        print()

if __name__ == "__main__":
    while True:
        pilihan = menu()
        
        if pilihan in [1, 2, 3, 4]:
            tampilkan_hasil_luas_keliling(pilihan)
            
        elif pilihan == 5:
            print("Terima kasih telah menggunakan program ini!")
            break
        
        else:
            print("Pilihan tidak valid.")
        
        input("Klik Enter untuk kembali ke menu...")
        cls()