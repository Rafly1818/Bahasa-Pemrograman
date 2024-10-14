def quick_sort(arr, low, high, step=1):
    if low < high:
        
        pi, step = partition(arr, low, high, step)
        

        step = quick_sort(arr, low, pi-1, step)
        step = quick_sort(arr, pi+1, high, step)
    return step
    
def partition(arr, low, high, step):
    i = (low - 1)
    pivot = arr[high]
    
    for j in range(low, high):
        
        if arr[j] <= pivot:
            i = i + 1 
            arr[i], arr[j], = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    print(f"Step {step}: {arr}")
    step += 1
    return i + 1, step
    
    
user_input = input("Masukkan angka-angka yang akan diurutkan, pisahkan dengan koma: ")

arr = [int(item) for item in user_input.split(",")]

print("Array sebelum diurutkan: ", arr)

quick_sort(arr, 0, len(arr) - 1)

print("Array setelah diurutkan: ", arr)