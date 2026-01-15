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