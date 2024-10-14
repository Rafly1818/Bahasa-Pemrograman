import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_perpustakaan(perpustakaan):
    penulis_sekarang = None
    for buku in perpustakaan:
        if buku['penulis'] != penulis_sekarang:
            if penulis_sekarang is not None:
                print("\n")  # Tambahkan spasi antara penulis yang berbeda
            penulis_sekarang = buku['penulis']
        print(f"Judul: {buku['judul']}\nPenulis: {buku['penulis']}\nTahun: {buku['tahun']}\n")

def cari_buku(perpustakaan, kata_kunci):
    hasil = [buku for buku in perpustakaan if kata_kunci.lower() in buku['judul'].lower() or kata_kunci.lower() in buku['penulis'].lower()]
    return hasil

def main():
    perpustakaan = [
        {"judul": "Laskar Pelangi", "penulis": "Andrea Hirata", "tahun": 2005},
        {"judul": "Sang Pemimpi", "penulis": "Andrea Hirata", "tahun": 2006},
        {"judul": "Sirkus Pohon", "penulis": "Andrea Hirata", "tahun": 2018},
        {"judul": "Pulang", "penulis": "Tere Liye", "tahun": 2015},
        {"judul": "Bumi", "penulis": "Tere Liye", "tahun": 2014},
        {"judul": "Matahari", "penulis": "Tere Liye", "tahun": 2016},
        {"judul": "Cinta Brontosaurus", "penulis": "Raditya Dika", "tahun": 2006},
        {"judul": "Koala Kumal", "penulis": "Raditya Dika", "tahun": 2015},
        {"judul": "Kambing Jantan", "penulis": "Raditya Dika", "tahun": 2017},
        {"judul": "Juru Bicara", "penulis": "Pandji Pragiwaksono", "tahun": 2016},
        {"judul": "Merdeka Dalam Bercanda", "penulis": "Pandji Pragiwaksono", "tahun": 2012},
        {"judul": "Menemukan Indonesia", "penulis": "Pandji Pragiwaksono", "tahun": 2016},
        {"judul": "Cantik Itu Luka", "penulis": "Eka Kurniawan", "tahun": 2002},
        {"judul": "Cantik Tak Ada Mati", "penulis": "Eka Kurniawan", "tahun": 2018},
        {"judul": "Sumur", "penulis": "Eka Kurniawan", "tahun": 2021},
    ]

    buku_terpilih = []
    
    while True:
        cls()
        print("Silahkan pilih menu")
        print()
        print("1. Daftar Buku")
        print("2. Pencarian Buku")
        print("3. Tampilkan Buku Terpilih")
        print("4. Keluar")
        
        pilihan = input("\nMasukkan pilihan anda: ")
        
        if pilihan == '1':
            cls()
            tampilkan_perpustakaan(perpustakaan)
            input("\nTekan Enter untuk kembali ke menu utama...")
        
        elif pilihan == '2':
            cls()
            kata_kunci = input("Masukkan judul atau penulis buku yang dicari: ")
            hasil_pencarian = cari_buku(perpustakaan, kata_kunci)
            cls()
            if hasil_pencarian:
                tampilkan_perpustakaan(hasil_pencarian)
                konfirmasi = input("\nApakah Anda ingin menyimpan buku ini untuk ditampilkan di daftar terpilih? (y/n): ")
                if konfirmasi.lower() == 'y':
                    buku_terpilih.extend(hasil_pencarian)
                    print("Buku telah disimpan ke daftar terpilih.")
                else:
                    print("Buku tidak disimpan.")
            else:
                print("Buku tidak ditemukan.")
            input("\nTekan Enter untuk kembali ke menu utama...")
        
        elif pilihan == '3':
            cls()
            if buku_terpilih:
                print("Buku Terpilih:\n")
                tampilkan_perpustakaan(buku_terpilih)
            else:
                print("Tidak ada buku terpilih untuk ditampilkan.")
            input("\nTekan Enter untuk kembali ke menu utama...")
        
        elif pilihan == '4':
            cls()
            print("Terimakasih sudah menggunakan program")
            break
        
        else:
            print("\nPilihan tidak valid. Silahkan coba lagi.")
            input("Tekan enter untuk kembali ke menu")

if __name__ == "__main__":
    main()
