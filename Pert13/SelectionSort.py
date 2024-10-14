def selection_sort(arr):
    n = len(arr)
    step = 1 
    
    for i in range(n):
        
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j 
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(f"Step {step}: {arr}")
        step += 1 


user_input = input("Masukkan angka-angka yang akan diurutkan, pisahkan dengan koma: ")

arr = [int(item) for item in user_input.split(",")]

print("Array sebelum diurutkan: ", arr)

selection_sort(arr)

print("Array setelah diurutkan: ", arr)