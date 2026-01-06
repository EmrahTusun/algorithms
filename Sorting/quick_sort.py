def partition(arr, low, high):
    # Pivot olarak son elemanı seçiyoruz
    pivot = arr[high]
    i = low - 1  # Küçük elemanların indeksi

    for j in range(low, high):
        # Eğer eleman pivottan küçükse sola al
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Pivotu doğru konumuna yerleştir
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        # Pivotun indeksini al
        pi = partition(arr, low, high)

        # Pivotun solu ve sağı için tekrar çağır
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

# Test
arr = [10, 7, 8, 9, 1, 5]
quick_sort(arr, 0, len(arr) - 1)
print("Quick Sort sonucu:", arr)