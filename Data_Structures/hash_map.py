class HashTable:
    def __init__(self, size=10):
        # Başlangıçta belirli boyutta boş kovalar (buckets) oluşturuyoruz
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        """
        Anahtarı (Key) bir indekse dönüştüren fonksiyon.
        Python'un gömülü hash() fonksiyonunu ve modulo operatörünü kullanıyoruz.
        """
        return hash(key) % self.size

    def set(self, key, value):
        """Anahtar-Değer çiftini ekler veya günceller"""
        index = self._hash(key)
        bucket = self.table[index]

        # Anahtar zaten var mı kontrol et, varsa güncelle
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value) # Güncelle
                return
        
        # Yoksa yeni ekle
        bucket.append((key, value))

    def get(self, key):
        """Anahtarın değerini getirir"""
        index = self._hash(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v
        
        return None # Bulunamazsa None döner

    def remove(self, key):
        """Anahtarı siler"""
        index = self._hash(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True
        return False

    def __str__(self):
        # Tabloyu okunaklı yazdırmak için
        result = []
        for i, bucket in enumerate(self.table):
            if bucket:
                result.append(f"Index {i}: {bucket}")
        return "\n".join(result)

# --- TEST ---
if __name__ == "__main__":
    ht = HashTable(size=10)

    ht.set("elma", 100)
    ht.set("muz", 200)
    ht.set("kiraz", 300)
    
    # Çakışma (Collision) testi için aynı indekse düşebilecek anahtarlar ekleyelim
    # (Hash fonksiyonuna göre değişebilir ama mantık aynıdır)
    
    print("Elma fiyatı:", ht.get("elma")) # 100
    
    ht.set("elma", 150) # Fiyatı güncelle
    print("Güncel elma fiyatı:", ht.get("elma")) # 150

    ht.remove("muz")
    print("Muz silindikten sonra:", ht.get("muz")) # None
    
    print("\nTablo Durumu:")
    print(ht)