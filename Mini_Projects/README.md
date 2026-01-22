# Fast Contact Manager (Hızlı Rehber)

Bu proje, standart veri yapıları yerine **kendi yazdığım Hash Map (Hash Table)** yapısını kullanarak geliştirilmiş bir rehber uygulamasıdır.

## Amaç
Teorik olarak öğrenilen **Hash Table** veri yapısının gerçek hayatta nasıl kullanıldığını göstermek. Hash Map sayesinde kişi sayısı 100 de olsa 1 milyon da olsa arama işlemi **$O(1)$** sürede gerçekleşir.

## Kullanılan Teknolojiler
* **Dil:** Python
* **Veri Yapısı:** Custom Hash Table with Chaining (Data_Structures klasöründen import edilmiştir).
* **Arayüz:** CLI (Komut Satırı Arayüzü)

## Nasıl Çalışır?
Uygulama, `Data_Structures/hash_map.py` modülünü import eder. İsimler "Key", telefon numaraları "Value" olarak saklanır.

---

# Stock Profit Bot (Borsa Robotu)

Geçmiş fiyat verilerini analiz ederek **maksimum karı** elde etmek için hangi gün alım ve hangi gün satım yapılması gerektiğini hesaplayan algoritma.

## Amaç
Veri seti üzerinde **tek geçiş (Single Pass)** yaparak en iyi sonucu bulmak. Bu problem, optimizasyon algoritmalarının klasik bir örneğidir.

## Nasıl Çalışır? (Algorithm Logic)
* **Naive Yaklaşım (Kötü):** Her gün için gelecekteki tüm günleri kontrol etmek. Karmaşıklık: $O(n^2)$.
* **Bizim Yaklaşımımız (İyi):** 1. İlerlerken gördüğümüz **en düşük fiyatı** (`min_price`) aklımızda tutarız.
  2. Her adımda "Bugün satarsam ne kadar kar ederim?" (`price - min_price`) diye bakarız.
  3. Eğer bu kar, rekor kardan fazlaysa güncelleriz.
  * **Karmaşıklık:** $O(n)$ (Linear Time) - Veri boyutu artsa da hız düşmez.

## Örnek
`Fiyatlar: [7, 1, 5, 3, 6, 4]`
* Robot 1. günde (7$) almaz.
* 2. günde fiyat 1$'a düştüğünde bunu "En Düşük" olarak işaretler.
* 5. günde fiyat 6$ olduğunda aradaki farkı (5$) hesaplar ve en yüksek kar olarak belirler.