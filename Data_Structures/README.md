# Data Structures

## 1. Linked List (Bağlı Liste)
**Tanım:** Verilerin bellekte ardışık olarak tutulmadığı, her elemanın (Node) bir sonraki elemanın adresini tuttuğu dinamik bir veri yapısıdır.

* **Yapısı:** `[Data | Next] -> [Data | Next] -> None`

### Dizi (Array) vs Linked List Karşılaştırması

| İşlem | Array (Dizi) | Linked List | Açıklama |
|-------|--------------|-------------|----------|
| **Erişim (Access)** | $O(1)$ | $O(n)$ | Dizide indeksten direkt bulursun, burada tek tek gezmen gerekir. |
| **Başa Ekleme** | $O(n)$ | $O(1)$ | Dizide herkesi kaydırmak gerekir, burada sadece başı değiştirirsin. |
| **Sona Ekleme** | $O(1)$* | $O(n)$ | *Dizi dolu değilse hızlıdır. Linked list'te sona gitmek zaman alır (Tail pointer yoksa). |
| **Silme (Deletion)** | $O(n)$ | $O(1)$* | *Silinecek elemanın yerini biliyorsan silmek çok hızlıdır. |

### Ne Zaman Kullanılmalı?
* **Linked List:** Sürekli veri ekleyip çıkaracaksan (özellikle baş taraftan) ve veri boyutu sürekli değişiyorsa.
* **Array:** Veriye hızlı erişmen gerekiyorsa (örn: `arr[500]`) ve boyut sabitse.

---

## 2. Stack (Yığın) - LIFO
**Mantık:** Last In First Out (Son Giren İlk Çıkar).
* **Kullanım Alanı:** "Geri Al" (Undo) işlemleri, Fonksiyon çağrıları (Recursion stack), Parantez kontrolü.

### Karmaşıklık Analizi
| İşlem | Zaman Karmaşıklığı | Açıklama |
|-------|--------------------|----------|
| **Push (Ekle)** | $O(1)$ | En tepeye koymak anlıktır. |
| **Pop (Çıkar)** | $O(1)$ | En tepeden almak anlıktır. |

---

## 3. Queue (Kuyruk) - FIFO
**Mantık:** First In First Out (İlk Giren İlk Çıkar).
* **Kullanım Alanı:** Yazıcı kuyrukları, İşletim sistemi işlem yönetimi, Breadth-First Search (BFS).
* **Önemli Not:** Python'da Queue için `list` yerine `collections.deque` kullanılmalıdır. Çünkü `list.pop(0)` işlemi $O(n)$ iken, `deque.popleft()` işlemi $O(1)$'dir.

### Karmaşıklık Analizi
| İşlem | Zaman Karmaşıklığı | Açıklama |
|-------|--------------------|----------|
| **Enqueue (Ekle)** | $O(1)$ | Sona eklemek. |
| **Dequeue (Çıkar)** | $O(1)$ | Baştan çıkarmak (deque ile). |

---

## 4. Binary Search Tree (BST)
**Tanım:** Her düğümün en fazla iki çocuğunun olduğu ve "Sol < Kök < Sağ" kuralına uyan ağaç yapısıdır.
* **Kullanım Alanı:** Veritabanı indeksleme, Dosya sistemleri, Sıralı veri tutma.

### Karmaşıklık Analizi
| İşlem | Ortalama (Dengeli Ağaç) | En Kötü (Dengesiz Ağaç) |
|-------|-------------------------|-------------------------|
| **Ekleme** | $O(\log n)$ | $O(n)$ |
| **Arama** | $O(\log n)$ | $O(n)$ |
| **Silme** | $O(\log n)$ | $O(n)$ |

> **Kritik Not:** Eğer sayıları sırayla eklerseniz (1, 2, 3, 4, 5...) ağaç bir çizgiye (Linked List) dönüşür ve performansı $O(n)$'e düşer. Bunu çözmek için **AVL Tree** veya **Red-Black Tree** gibi "kendini dengeleyen" ağaçlar kullanılır.