def vending_machine(kembalian):
    pecahan = [100000, 50000, 20000, 10000, 5000]
    hasil = {}
    
    for p in pecahan:
        if kembalian >= p:
            hasil[p] = kembalian // p
            kembalian = kembalian % p
        
    return hasil

def format_rupiah(angka):
    return f"Rp {angka:,.0f}".replace(',', '.')

def hitung_diskon(harga, persen_diskon):
    return harga * persen_diskon / 100

def soalnomor_1():
    global running  # Menggunakan variabel global untuk mengontrol loop
    print()
    print("Soal Pertama!!")
    print("Buatlah Program (python) untuk memberikan kembalian pada mesin penjual otomatis.")
    
    harga_produk = 5000
    print(f"Harga produk : {format_rupiah(harga_produk)}")
    
    print()
    jumlah_beli = int(input("Masukkan jumlah pembelian : "))
    jumlah_uang = int(input("Masukkan uang anda : "))
    total_beli = harga_produk * jumlah_beli

    if jumlah_uang < total_beli:
        print("Maaf, uang yang anda masukkan tidak cukup")
        print("Kembali ke menu awal")
        print()
        return
    
    kembalian = jumlah_uang - total_beli
    pecahan_kembalian = vending_machine(kembalian)
    print()
    
    print(f"Total pembelian : {format_rupiah(total_beli)}")
    print(f"Uang yang diberikan : {format_rupiah(jumlah_uang)}")
    print(f"Kembalian : {format_rupiah(kembalian)}")
    print()
    
    print("Pecahan kembalian")
    for k, v in pecahan_kembalian.items():
        print(f"Pecahan {format_rupiah(k)}: {v} lembar")
    print()
    running = False  # Menghentikan loop setelah soal nomor 1 selesai

def soalnomor_2():
    global running  # Menggunakan variabel global untuk mengontrol loop
    print()
    print("Soal Kedua!!")
    print("Sebuah toko yang sedang mengobral barang-barangnya membuat aturan diskon sebagai berikut.")
    
    print()
    print("Pilih salah satu dari dua pilihan berikut:")
    print("1. Barang Baru")
    print("2. Barang Lama")
    pilihan_2 = input("Masukkan pilihan Anda (1/2): ")
    
    if pilihan_2 == "1":
        print()
        print("Peraturan!!")
        print("Jika barang tersebut adalah barang baru, maka aturannya adalah sebagai berikut:")
        print("1. Jika harga barang adalah Rp 0 – Rp 200.000, maka diskon adalah 10%")
        print("2. Jika harga barang adalah Rp 200.001 – Rp 500.000, maka diskon adalah 15%")
        print("3. Jika harga barang di atas Rp 500.000, maka diskon adalah 20%.")
        
        print()
        harga_satuan = int(input("Masukkan harga satuan barang: "))
        jumlah_barang = int(input("Masukkan jumlah barang yang ingin dibeli: "))
        total_harga = harga_satuan * jumlah_barang
        
        if total_harga <= 200000:
            diskon = hitung_diskon(total_harga, 10)
        elif total_harga <= 500000:
            diskon = hitung_diskon(total_harga, 15)
        else:
            diskon = hitung_diskon(total_harga, 20)
   
    elif pilihan_2 == "2":
        print()
        print("Peraturan!!")
        print("Jika barang tersebut adalah barang lama, maka aturannya adalah sebagai berikut:")
        print("1. Jika harga barang adalah Rp 0 – Rp 100.000, maka diskon adalah 15%")
        print("2. Jika harga barang adalah Rp 100.001 – Rp 250.000, maka diskon adalah 20%")
        print("3. Jika harga barang di atas Rp 250.000, maka diskon adalah 25%") 
        
        print()
        harga_satuan = int(input("Masukkan harga satuan barang: "))
        jumlah_barang = int(input("Masukkan jumlah barang yang ingin dibeli: "))
        total_harga = harga_satuan * jumlah_barang
        
        if total_harga <= 100000:
            diskon = hitung_diskon(total_harga, 15)
        elif total_harga <= 250000:
            diskon = hitung_diskon(total_harga, 20)
        else:
            diskon = hitung_diskon(total_harga, 25)
    
    else:
        print("Pilihan tidak valid.")
        return
    
    harga_setelah_diskon = total_harga - diskon
    print()
    print(f"Harga satuan: {format_rupiah(harga_satuan)}")
    print(f"Jumlah barang: {jumlah_barang}")
    print(f"Total harga sebelum diskon: {format_rupiah(total_harga)}")
    print(f"Diskon: {format_rupiah(diskon)}")
    print(f"Total harga setelah diskon: {format_rupiah(harga_setelah_diskon)}")
    print()
    running = False  # Menghentikan loop setelah soal nomor 2 selesai
    
pilihan = {
    "1": soalnomor_1,
    "2": soalnomor_2,
}

running = True

while running:
    print("SOAL UTS")
    print()
    print("1. Soal Pertama")
    print("2. Soal Kedua")
    print("3. Exit")
    print()
    pilihan_pengguna = input("Masukkan pilihan Anda (1/2/3) : ")

    if pilihan_pengguna in pilihan:
       pilihan[pilihan_pengguna]()
    elif pilihan_pengguna == "3":
        break
    else:
        print("Pilihan tidak valid.")