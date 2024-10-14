import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def sequential_search(library, title):
    for book in library:
        if book['title'].lower() == title.lower():
            return book
    return None

def is_prime(num):
    """Mengecek apakah sebuah angka merupakan bilangan prima."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

def display_library(library):
    print("Daftar buku yang tersedia di perpustakaan:\n")
    for book in library:
        print(f"Judul: {book['title']}, Penulis: {book['author']}, Tahun: {book['year']}")

def main():
    library = [
        {"title": "Laskar Pelangi", "author": "Andrea Hirata", "year": 2005},
        {"title": "Bumi Manusia", "author": "Pramoedya Ananta Toer", "year": 1980},
        {"title": "Pulang", "author": "Leila S. Chudori", "year": 2012},
        {"title": "5 Cm", "author": "Donny Dhirgantoro", "year": 2005},
        {"title": "Negeri 5 Menara", "author": "Ahmad Fuadi", "year": 2009},
        {"title": "Ayat-Ayat Cinta", "author": "Habiburrahman El Shirazy", "year": 2004},
        {"title": "Supernova", "author": "Dee Lestari", "year": 2001},
        {"title": "Ronggeng Dukuh Paruk", "author": "Ahmad Tohari", "year": 1982},
    ]

    while True:
        cls()
        print("Pilih operasi pencarian:")
        print()
        print("1. Sequential Search (Buku)")
        print("2. Cek Bilangan Prima (Angka)")
        print("3. Binary Search (Angka)")
        print("4. Keluar")

        pilihan = input("\nMasukkan pilihan Anda: ")

        if pilihan == '1':
            cls()
            display_library(library)
            title_to_search = input("\nMasukkan judul buku yang ingin dicari (Sequential Search): ")

            result = sequential_search(library, title_to_search)
            if result:
                print("\nBuku ditemukan")
                print(f"Judul: {result['title']}")
                print(f"Penulis: {result['author']}")
                print(f"Tahun: {result['year']}")
            else:
                print("\nBuku tidak ditemukan.")
            
            input("\nTekan Enter untuk kembali ke menu.")
        
        elif pilihan == '2':
            cls()
            num_to_check = int(input("\nMasukkan angka yang ingin dicek apakah prima: "))

            if is_prime(num_to_check):
                print(f"\n{num_to_check} adalah bilangan prima.")
            else:
                print(f"\n{num_to_check} bukan bilangan prima.")
            
            input("\nTekan Enter untuk kembali ke menu.")
        
        elif pilihan == '3':
            cls()
            arr = list(map(int, input("Masukkan daftar elemen yang sudah terurut (pisahkan dengan spasi): ").split()))
            x = int(input("Masukkan elemen yang akan dicari: "))

            result = binary_search(arr, x)

            if result != -1:
                print(f"\nElemen ditemukan pada indeks {result}")
            else:
                print("\nElemen tidak ditemukan dalam daftar")
            
            input("\nTekan Enter untuk kembali ke menu.")

        elif pilihan == '4':
            print("Terima kasih telah menggunakan program pencarian.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            input("\nTekan Enter untuk kembali ke menu.")

if __name__ == "__main__":
    main()
