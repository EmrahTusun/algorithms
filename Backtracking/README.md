# Backtracking Algorithms

Backtracking, bir problemin çözümünü adım adım inşa eden, bir adımın çözüme götürmeyeceğini anladığında o adımı iptal edip (geri dönüp) başka bir yol deneyen algoritmik bir tekniktir.

## 1. N-Queens Problem
**Amaç:** $NxN$ boyutundaki bir satranç tahtasına $N$ adet veziri, hiçbiri birbirini tehdit etmeyecek şekilde yerleştirmek.

### Çalışma Mantığı
1. İlk sütundan başla.
2. Mevcut sütunda veziri koyabileceğin güvenli bir satır bul.
3. Veziri koy ve bir sonraki sütun için fonksiyonu tekrar çağır (Recursion).
4. Eğer bir sonraki sütunda çözüm bulunamazsa, veziri kaldır (Backtrack) ve bir sonraki satırı dene.

### Karmaşıklık Analizi
| Durum | Zaman Karmaşıklığı | Açıklama |
|-------|--------------------|----------|
| **En Kötü (Worst)** | $O(N!)$ | Faktöriyel zaman. Olası tüm yerleşimleri dener. |

> **Not:** $O(N!)$ bilgisayar bilimlerindeki en yavaş karmaşıklık türlerinden biridir. Ancak bu tür kombinasyon problemlerinde (tüm olasılıkları deneme) kaçınılmazdır.