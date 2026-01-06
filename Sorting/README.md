# Sorting Algorithms Analysis

## 1. Bubble Sort
**Tanım:** Yan yana duran elemanları karşılaştırıp yanlış sıradaysalar yerlerini değiştiren (swap) temel bir sıralama algoritmasıdır.

### Karmaşıklık Analizi (Complexity Analysis)
| Durum | Zaman Karmaşıklığı (Time Complexity) | Açıklama |
|-------|-------------------------------------|----------|
| **En İyi (Best)** | $O(n)$ | Dizi zaten sıralıysa (Optimize edilmiş kodda). |
| **Ortalama (Avg)** | $O(n^2)$ | Elemanlar rastgele dağılmışsa. |
| **En Kötü (Worst)** | $O(n^2)$ | Dizi tersten sıralıysa. |

* **Alan Karmaşıklığı (Space Complexity):** $O(1)$ (Ekstra hafıza kullanmaz, in-place çalışır).

### Çalışma Mantığı
Dizi üzerinde defalarca geçiş yapar. Her geçişte en büyük eleman "baloncuk" gibi dizinin sonuna yükselir.