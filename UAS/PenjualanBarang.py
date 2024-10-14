import os

def cls():
  """Membersihkan layar konsol."""
  os.system('cls' if os.name == 'nt' else 'clear')

def format_rupiah(angka):
  """Memformat angka menjadi format rupiah."""
  return f"Rp {angka:,}"

def tambah_barang():
  cls()
  print("Isi Data Barang")
  print()
  nama = input("Masukkan nama barang: ")
  harga = int(input("Masukkan harga barang: "))
  stok = int(input("Masukkan stok barang: "))
  barang.append({'nama': nama, 'harga': harga, 'stok': stok})
  print()
  print("Data barang berhasil ditambahkan!")
  input("Tekan Enter untuk kembali ke menu...")

def tampil_barang():
  cls()
  if len(barang) == 0:
    print("Tidak ada data barang.")
  else:
    print("Data Barang")
    print()
    for i, b in enumerate(barang):
      print(f"{i+1}. Nama  : {b['nama']}")
      print(f"   Harga : {format_rupiah(b['harga'])}")
      print(f"   Stok  : {b['stok']}")
    print() 
  input("Tekan Enter untuk kembali ke menu...")

def hapus_barang():
  cls()
  print("Hapus Barang")
  print()
  nama = input("Masukkan nama barang yang ingin dihapus: ")
  for i, b in enumerate(barang):
    if b['nama'] == nama:
      del barang[i]
      print("Data barang berhasil dihapus!")
      print()
      input("Tekan Enter untuk kembali ke menu...")
      return
  print("Data barang tidak ditemukan.")
  print()
  input("Tekan Enter untuk kembali ke menu...")

def cari_barang():
  cls()
  print("Pencarian Barang")
  print()
  nama = input("Masukkan nama barang yang ingin dicari: ")
  found = False
  for b in barang:
    if b['nama'] == nama:
      print(f"\nNama: {b['nama']}")
      print(f"Harga: {format_rupiah(b['harga'])}")
      print(f"Stok: {b['stok']}")
      found = True
      break
  if not found:
    print("\nData barang tidak ditemukan.")
  input("\nTekan Enter untuk kembali ke menu...")

def hitung_pembelian():
  cls()
  print("Pembelian Barang")
  print()
  nama = input("Masukkan nama barang yang ingin dibeli: ")
  found = False
  for b in barang:
    if b['nama'] == nama:
      found = True
      jumlah = int(input("Masukkan jumlah yang ingin dibeli: "))
      if b['stok'] >= jumlah:
        b['stok'] -= jumlah
        total_harga = jumlah * b['harga']
        print(f"\nTotal harga: {format_rupiah(total_harga)}")
      else:
        print("\nStok barang tidak mencukupi.")
      break
  if not found:
    print("\nData barang tidak ditemukan.")
  input("\nTekan Enter untuk kembali ke menu...")

barang = []

while True:
  cls()
  print("Silahkan pilih menu yang anda inginkan")
  print()
  print("1. Tambah barang")
  print("2. Tampilkan barang")
  print("3. Hapus barang")
  print("4. Cari barang")
  print("5. Hitung pembelian")
  print("6. Exit")
  print()
  pilihan = input("Masukkan pilihan: ")

  if pilihan == '':
    continue  # Kembali ke awal loop jika input kosong
  elif pilihan == '1':
    tambah_barang()
  elif pilihan == '2':
    tampil_barang()
  elif pilihan == '3':
    hapus_barang()
  elif pilihan == '4':
    cari_barang()
  elif pilihan == '5':
    hitung_pembelian()
  elif pilihan == '6':
    break
  else:
    print("Pilihan tidak valid.")
    input("Tekan Enter untuk kembali ke menu...")
