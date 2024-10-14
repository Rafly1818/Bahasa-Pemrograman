def insertion_sort(arr):
    step = 1 
    
    for i in range(1, len(arr)):
        key = arr[i]
        
        
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1 
        arr[j + 1] = key
        print(f"Step {step}: {arr}")
        step += 1


user_input = input("Masukkan angka-angka yang akan diurutkan, pisahkan dengan koma: ")

arr = [int(item) for item in user_input.split(",")]

print("Array sebelum diurutkan: ", arr)

insertion_sort(arr)

print("Array setelah diurutkan: ", arr)