def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

user_input = input("Masukkan nilai n untuk deret Fibonacci : ")
try:
    n = int(user_input)
    print(f"Nilai Fibonacci ke-{n} adalah {fibonacci(n)}")
except ValueError:
    print("Masukkan angka yang valid.")