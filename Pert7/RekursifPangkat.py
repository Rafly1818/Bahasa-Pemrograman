def pangkat(base, exp):
    if exp == 0:
        return 1 #Setiap bilangan dipangkat 0 hasilnya adalah 1
    elif exp > 0:
        return base * pangkat(base, exp - 1) #pangkat positif
    else:
        return 1 / pangkat(base, -exp) #pangkat negatif


base_input = input("Masukkan bilangan dasar : ")
exp_input = input("Masukkan eksponen (pangkat) : ")

try:
    base = float(base_input)
    exp = int(exp_input)
    hasil = pangkat(base, exp)
    print(f"{base} dipangkatkan dengan {exp} adalah {hasil}")
    
except ValueError:
    print("Pastikan bilangan dasar adalah angka dan eksponen adalah bilangan bulat.")