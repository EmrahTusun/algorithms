def merge_sort(arr):
    if len(arr) > 1:
        # Diziyi ortadan ikiye böl
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Her iki parçayı recursive (özyinelemeli) olarak sırala
        merge_sort(left_half)
        merge_sort(right_half)

        # İki sıralı parçayı birleştir (Merge işlemi)
        i = j = k = 0

        # İki listeyi karşılaştırarak ana listeye yaz
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Varsa artan elemanları ekle
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Test
arr = [12, 11, 13, 5, 6, 7]
merge_sort(arr)
print("Merge Sort sonucu:", arr)