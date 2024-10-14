def baca_file(nama_file):
    try:
        with open(nama_file, 'r') as file:
            isi = file.read()
            print("Isi file:")
            print(isi)
    except FileNotFoundError:
        print(f"File '{nama_file}' tidak ditemukan.")
    except IOError:
        print(f"Terjadi kesalahan saat membaca file '{nama_file}'.")

# Nama file yang ingin dibaca
nama_file = "contoh.txt"

# Panggil fungsi untuk membaca file
baca_file(nama_file)