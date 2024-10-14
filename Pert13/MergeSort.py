def merge_sort(arr, step=1):
    """
    Fungsi untuk mengurutkan array menggunakan algoritma Merge Sort.

    Parameter:
        arr (list): Array yang ingin diurutkan.
        step (int, opsional): Langkah untuk menampilkan proses pengurutan.

    Returns:
        list: Array yang sudah diurutkan.
    """

    if len(arr) <= 1:
        return arr

    # Menentukan titik tengah array
    mid = len(arr) // 2

    # Membagi array menjadi dua bagian kiri dan kanan
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Mengurutkan bagian kiri dan kanan secara rekursif
    merge_sort(left_half, step)
    merge_sort(right_half, step)

    # Menggabungkan bagian kiri dan kanan yang sudah diurutkan
    i = 0
    j = 0
    k = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    # Menambahkan elemen yang tersisa di bagian kiri atau kanan
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1

    # Menampilkan proses pengurutan (opsional)
    if step > 1:
        print(f"Step ({step}): {arr}")

    return arr

user_input = input("Masukkan angka-angka yang akan diurutkan, pisahkan dengan koma: ")
arr = [int(item) for item in user_input.split(",")]

# Menampilkan array sebelum diurutkan
print("Array sebelum diurutkan:", arr)

# Mengurutkan array
arr = merge_sort(arr)

# Menampilkan array setelah diurutkan
print("Array setelah diurutkan:", arr)

