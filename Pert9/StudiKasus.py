import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def format_rupiah(amount):
    amount_str = f"{amount:,.2f}"  # Format to 2 decimal places
    amount_str = amount_str.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"Rp. {amount_str}"

# Fungsi dari studi kasus 1
def input_data_mahasiswa():
    cls()
    mahasiswa = []
    jumlah = int(input("Masukkan jumlah mahasiswa: "))
    for i in range(jumlah):
        nama = input(f"Masukkan nama mahasiswa ke-{i+1}: ")
        nim = input(f"Masukkan NIM mahasiswa ke-{i+1}: ")
        prodi = input(f"Masukkan prodi mahasiswa ke-{i+1}: ")
        nilai = float(input(f"Masukkan nilai mahasiswa ke-{i+1}: "))
        mahasiswa.append({'nama': nama, 'nim': nim, 'prodi': prodi, 'nilai': nilai})
    return mahasiswa


def tampilkan_data_mahasiswa(mahasiswa):
    cls()
    print("Data Mahasiswa")
    print()
    for m in mahasiswa:
        print(f"Nama: {m['nama']}")
        print(f"NIM: {m['nim']}")
        print(f"Prodi: {m['prodi']}")
        print(f"Nilai: {m['nilai']}")
        print()


def hitung_rata2_nilai(mahasiswa):
    if not mahasiswa:
        return 0
    total_nilai = sum(m['nilai'] for m in mahasiswa)
    return total_nilai / len(mahasiswa)


def cari_nilai_mahasiswa(mahasiswa):
    if not mahasiswa:
        return None, None
    mahasiswa_tertinggi = max(mahasiswa, key=lambda x: x['nilai'])
    mahasiswa_terendah = min(mahasiswa, key=lambda x: x['nilai'])
    return mahasiswa_tertinggi, mahasiswa_terendah


# Fungsi dari studi kasus 2
def input_data_barang(barang):
    cls()
    jumlah = int(input("Masukkan jumlah barang: "))
    for i in range(jumlah):
        nama = input(f"Masukkan nama barang ke-{i+1}: ")
        kode = input(f"Masukkan kode barang ke-{i+1}: ")
        jumlah_barang = int(input(f"Masukkan jumlah barang ke-{i+1}: "))
        barang.append({'nama': nama, 'kode': kode, 'jumlah': jumlah_barang})
    return barang


def tampilkan_data_barang(barang):
    cls()
    print("Data Barang")
    print()
    for b in barang:
        print(f"Nama: {b['nama']}")
        print(f"Kode: {b['kode']}")
        print(f"Jumlah Barang: {b['jumlah']}")
        print()


def mencari_barang_berdasarkan_kode(barang, kode):
    cls()
    for b in barang:
        if b['kode'] == kode:
            return b
    return None


def hapus_barang_berdasarkan_kode(barang, kode):
    cls()
    for b in barang:
        if b['kode'] == kode:
            barang.remove(b)
            return True
    return False


# Fungsi dari studi kasus 3
def input_data_transaksi():
    cls()
    transaksi = []
    jumlah = int(input("Masukkan jumlah transaksi: "))
    for i in range(jumlah):
        jenis = input(f"Masukkan jenis transaksi ke-{i+1} (pemasukan/pengeluaran): ")
        jumlah_transaksi = float(input(f"Masukkan jumlah transaksi ke-{i+1}: Rp. "))
        transaksi.append({'jenis': jenis, 'jumlah': jumlah_transaksi})
    return transaksi


def tampilkan_data_transaksi(transaksi):
    cls()
    print("Data Transaksi:")
    for t in transaksi:
        print(f"Jenis: {t['jenis']}, Jumlah: {format_rupiah(t['jumlah'])}")
    print()


def hitung_total_pemasukan(transaksi):
    return sum(t['jumlah'] for t in transaksi if t['jenis'] == 'pemasukan')


def hitung_total_pengeluaran(transaksi):
    return sum(t['jumlah'] for t in transaksi if t['jenis'] == 'pengeluaran')


def hitung_saldo_akhir(transaksi):
    pemasukan = hitung_total_pemasukan(transaksi)
    pengeluaran = hitung_total_pengeluaran(transaksi)
    return pemasukan - pengeluaran


def menu():
    cls()
    print("Studi Kasus")
    print()
    print("1. Data Mahasiswa")
    print("2. Inventaris Barang")
    print("3. Pengelolaan Keuangan Pribadi")
    print("4. Exit")


def menu_mahasiswa():
    cls()
    print("Studi Kasus 1 (Data Mahasiswa)")
    print()
    print("1. Input data mahasiswa")
    print("2. Tampilkan data mahasiswa")
    print("3. Hitung rata-rata nilai mahasiswa")
    print("4. Cari mahasiswa dengan nilai tertinggi dan terendah")
    print("5. Kembali ke menu utama")


def menu_barang():
    cls()
    print("Studi Kasus 2 (Inventaris Barang)")
    print()
    print("1. Input data barang")
    print("2. Tampilkan data barang")
    print("3. Cari barang berdasarkan kode")
    print("4. Hapus barang berdasarkan kode")
    print("5. Kembali ke menu utama")


def menu_keuangan():
    cls()
    print("Studi Kasus 3 (Pengelolaan Keuangan Pribadi)")
    print()
    print("1. Input data transaksi")
    print("2. Tampilkan data transaksi")
    print("3. Hitung total pemasukan")
    print("4. Hitung total pengeluaran")
    print("5. Hitung saldo akhir")
    print("6. Kembali ke menu utama")


def main():
    mahasiswa = []
    barang = []
    transaksi = []

    while True:
        menu()
        print()
        pilihan = input("Masukkan Pilihan Anda: ")
        if pilihan == "1":
            while True:
                menu_mahasiswa()
                print()
                sub_pilihan = input("Masukkan Pilihan Anda: ")
                if sub_pilihan == "1":
                    mahasiswa = input_data_mahasiswa()
                elif sub_pilihan == "2":
                    tampilkan_data_mahasiswa(mahasiswa)
                elif sub_pilihan == "3":
                    print()
                    rata_rata = hitung_rata2_nilai(mahasiswa)
                    print(f"Rata-rata nilai mahasiswa: {rata_rata}")
                elif sub_pilihan == "4":
                    tertinggi, terendah = cari_nilai_mahasiswa(mahasiswa)
                    print(f"Mahasiswa dengan nilai tertinggi: {tertinggi}")
                    print(f"Mahasiswa dengan nilai terendah: {terendah}")
                elif sub_pilihan == "5":
                    break
                else:
                    print("Pilih yang benar.")
                input("Tekan Enter untuk melanjutkan...")
        elif pilihan == "2":
            while True:
                menu_barang()
                print()
                sub_pilihan = input("Masukkan Pilihan Anda: ")
                if sub_pilihan == "1":
                    barang = input_data_barang(barang)
                elif sub_pilihan == "2":
                    tampilkan_data_barang(barang)
                elif sub_pilihan == "3":
                    kode = input("Masukkan kode barang yang dicari: ")
                    hasil = mencari_barang_berdasarkan_kode(barang, kode)
                    if hasil:
                        print(f"Barang berhasil ditemukan: {hasil}")
                    else:
                        print("Barang tidak ditemukan.")
                elif sub_pilihan == "4":
                    kode = input("Masukkan kode barang yang ingin dihapus: ")
                    if hapus_barang_berdasarkan_kode(barang, kode):
                        print("Barang berhasil dihapus.")
                    else:
                        print("Barang tidak ditemukan.")
                elif sub_pilihan == "5":
                    break
                else:
                    print("Pilih yang benar.")
                input("Tekan Enter untuk melanjutkan...")
        elif pilihan == "3":
            while True:
                menu_keuangan()
                print()
                sub_pilihan = input("Masukkan Pilihan Anda: ")
                if sub_pilihan == "1":
                    transaksi = input_data_transaksi()
                elif sub_pilihan == "2":
                    tampilkan_data_transaksi(transaksi)
                elif sub_pilihan == "3":
                    total_pemasukan = hitung_total_pemasukan(transaksi)
                    print(f"Total pemasukan: {format_rupiah(total_pemasukan)}")
                elif sub_pilihan == "4":
                    total_pengeluaran = hitung_total_pengeluaran(transaksi)
                    print(f"Total pengeluaran: {format_rupiah(total_pengeluaran)}")
                elif sub_pilihan == "5":
                    saldo_akhir = hitung_saldo_akhir(transaksi)
                    print(f"Saldo akhir: {format_rupiah(saldo_akhir)}")
                elif sub_pilihan == "6":
                    break
                else:
                    print("Pilih yang benar.")
                input("Tekan Enter untuk melanjutkan...")
        elif pilihan == "4":
            break
        else:
            print("Pilih yang benar.")
        input("Tekan Enter untuk melanjutkan...")


if __name__ == "__main__":
    main()
