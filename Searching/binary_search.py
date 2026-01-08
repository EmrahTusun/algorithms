def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == target:
            return mid
        if guess > target:
            high = mid - 1  # Aranan sol tarafta
        else:
            low = mid + 1   # Aranan sağ tarafta
            
    return -1

# Test (Dizi sıralı olmak zorunda!)
data = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
aranan = 23
sonuc = binary_search(data, aranan)

if sonuc != -1:
    print(f"Eleman {sonuc}. indekste bulundu.")
else:
    print("Eleman bulunamadı.")