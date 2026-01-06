def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # En küçük elemanın indeksini bul
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        # Bulunan en küçük elemanı en başa (i'nin yerine) al
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Test
arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print("Selection Sort sonucu:", arr)