def input_angka():
    try:
        angka1 = int(input("Masukkan angka pertama : "))
        angka2 = int(input("Masukkan angka kedua : "))
        
        print()
        result1 = (angka1, angka2)
        result2 = angka1 / angka2
        
        print(f"Angka dalam ineteger adalah : {result1}")
        print(f"hasil pembagian adalah : {int(result2)}")
        
    except ZeroDivisionError:
        print("Tidak bisa membagi dengan nol.")
    except ValueError:
        print("Input angka bukan huruf.")
    finally:
        print("Suksess")
            
input_angka()