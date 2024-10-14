def s(n, steps):
    if n == 1:
        steps.append(f"S({n}) = {n}")
        return n
    else:
        result = n + s(n - 1, steps)
        steps.append(f"S({n}) = {n} + S({n-1}) = {result}")
        return result

n = int(input("Masukkan nilai n: "))

steps = []

hasil = s(n, steps)

print(" | ".join(steps))
print(f"Hasil deret S = {hasil}")