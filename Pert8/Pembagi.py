class DivisionError(Exception):
    pass

def bagi(angka1, angka2):
    try:
        if angka2 == 0:
            raise DivisionError("Tidak bisa membagi dengan nol.")
        return angka1 / angka2
    except DivisionError as e:
        print(e)

def main():
    try:
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))
        
        hasil = bagi(angka1, angka2)
        if hasil is not None:
            print(f"Hasil pembagian adalah: {hasil}")
    except ValueError:
        print("Input harus berupa angka.")


main()