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

---

## 2. Selection Sort
**Tanım:** Dizideki en küçük elemanı bulup en başa koyarak ilerleyen algoritmadır.

### Karmaşıklık Analizi
| Durum | Zaman Karmaşıklığı | Açıklama |
|-------|--------------------|----------|
| **Hepsi** | $O(n^2)$ | Dizi sıralı olsa bile her elemanı kontrol eder. |

* **Alan:** $O(1)$
* **Not:** Bellek yazma işlemi (swap) sayısı azdır, bu yüzden yazma maliyeti yüksek belleklerde Bubble Sort'tan iyidir.

---

## 3. Insertion Sort
**Tanım:** Her elemanı, kendinden önceki sıralı alt dizi içinde doğru yere yerleştirir.

### Karmaşıklık Analizi
| Durum | Zaman Karmaşıklığı | Açıklama |
|-------|--------------------|----------|
| **En İyi** | $O(n)$ | Dizi zaten sıralıysa sadece kontrol edip geçer. |
| **En Kötü** | $O(n^2)$ | Dizi tersten sıralıysa. |

* **Alan:** $O(1)$
* **Not:** Küçük veri setlerinde ve neredeyse sıralı dizilerde çok hızlıdır.

---

## 4. Merge Sort
**Tanım:** Diziyi sürekli ikiye bölüp, en küçük parçadan başlayarak sıralı şekilde birleştiren (Divide and Conquer) algoritmadır.

### Karmaşıklık Analizi
| Durum | Zaman Karmaşıklığı | Açıklama |
|-------|--------------------|----------|
| **Hepsi** | $O(n \log n)$ | Her durumda diziyi böler ve birleştirir. Garantili performans sağlar. |

* **Alan:** $O(n)$ (Yardımcı diziler için ekstra bellek gerekir).
* **Not:** Büyük veri setleri için çok uygundur (Stable sort'tur).

---

## 5. Quick Sort
**Tanım:** Bir "pivot" eleman seçip, ondan küçükleri sola, büyükleri sağa atarak ilerleyen algoritmadır.

### Karmaşıklık Analizi
| Durum | Zaman Karmaşıklığı | Açıklama |
|-------|--------------------|----------|
| **Ortalama** | $O(n \log n)$ | Genellikle en hızlı çalışan sıralama algoritmasıdır. |
| **En Kötü** | $O(n^2)$ | Pivot hep en büyük/küçük eleman seçilirse (Nadir). |

* **Alan:** $O(\log n)$ (Recursion stack için).
* **Not:** Merge Sort'a göre daha az bellek harcar ama "Worst Case" riski vardır.