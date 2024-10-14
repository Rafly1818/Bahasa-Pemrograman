def bubble_sort(arr):
    n = len(arr)
    step = 1 
    
    for i in range(n):
        swapped =False
        
        for j in range(0, n-i-1):
            
            
            
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
            print(f"Step {step}: {arr}")
            step += 1 
            
        if not swapped:
            break

user_input = input("Masukkan angka-angka yang akan di urutkan, pisahkan dengan koma: ")

arr = [int(item) for item in user_input.split(",")]

print("Array sebelum diurutkan: ", arr)

bubble_sort(arr)

print("Array setelah diurutkan: ", arr)
