def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Key'den büyük olan elemanları bir sağa kaydır
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Test
arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print("Insertion Sort sonucu:", arr)