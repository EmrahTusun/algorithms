def linear_search(arr, target):
    """
    Diziyi baştan sona tarar. Bulursa indeksini, bulamazsa -1 döner.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Test
data = [10, 50, 30, 70, 80, 20]
aranan = 30
sonuc = linear_search(data, aranan)

if sonuc != -1:
    print(f"Eleman {sonuc}. indekste bulundu.")
else:
    print("Eleman bulunamadı.")