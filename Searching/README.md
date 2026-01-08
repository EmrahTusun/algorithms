# Searching Algorithms

## 1. Linear Search (Doğrusal Arama)
**Mantık:** Dizinin başından başlayarak aranan elemanı bulana kadar tek tek kontrol eder.
* **Avantajı:** Veri sıralı olmak zorunda değildir.
* **Dezavantajı:** Büyük veri setlerinde çok yavaştır.

## 2. Binary Search (İkili Arama)
**Mantık:** "Böl ve Yönet" prensibiyle çalışır. Sıralı bir dizinin ortasına bakar; aranan değer ortadakinden büyükse sağa, küçükse sola giderek arama uzayını her adımda yarıya indirir.
* **Ön Şart:** Dizi mutlaka **sıralı** olmalıdır.

### Karmaşıklık Karşılaştırması (Complexity Analysis)

| Algoritma | Time (Best) | Time (Average) | Time (Worst) | Space Complexity |
|-----------|-------------|----------------|--------------|------------------|
| **Linear Search** | $O(1)$ | $O(n)$ | $O(n)$ | $O(1)$ |
| **Binary Search** | $O(1)$ | $O(\log n)$ | $O(\log n)$ | $O(1)$ (Iterative) |

> **Örnek:** 1 Milyon elemanlı bir listede:
> * **Linear Search** en kötü durumda 1.000.000 adım atar.
> * **Binary Search** en kötü durumda sadece **20 adım** atar ($log_2 1.000.000 \approx 20$).