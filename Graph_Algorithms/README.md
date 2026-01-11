# Graph Traversal Algorithms

Graf üzerinde gezinme algoritmaları, ağ yapılarını analiz etmek için kullanılır.

## 1. BFS (Breadth-First Search)
**Mantık:** Bir düğümden başlar ve önce tüm doğrudan komşularını (kardeşlerini) gezer, sonra bir alt seviyeye iner. "Katman katman" ilerler.
* **Veri Yapısı:** Queue (Kuyruk - FIFO) kullanılır.
* **Kullanım Alanı:** En kısa yolu bulma (Shortest Path in Unweighted Graph), Sosyal ağlarda "arkadaşın arkadaşı" analizi.

## 2. DFS (Depth-First Search)
**Mantık:** Bir düğümden başlar ve gidebildiği kadar derine (bir dalın sonuna kadar) gider, sonra geri döner (backtrack).
* **Veri Yapısı:** Stack (Yığın - LIFO) veya Recursion (Özyineleme) kullanılır.
* **Kullanım Alanı:** Labirent çözme, Döngü tespiti (Cycle Detection).

### Karmaşıklık Analizi (Complexity Analysis)

Graf algoritmalarında $V$: Düğüm Sayısı (Vertices), $E$: Kenar Sayısı (Edges) olarak ifade edilir.

| Algoritma | Zaman Karmaşıklığı | Alan Karmaşıklığı |
|-----------|--------------------|-------------------|
| **BFS** | $O(V + E)$ | $O(V)$ |
| **DFS** | $O(V + E)$ | $O(V)$ |

> **Not:** Adjacency List (Komşuluk Listesi) kullanıldığı varsayılmıştır. Adjacency Matrix kullanılsaydı zaman karmaşıklığı $O(V^2)$ olurdu.

---

## 3. Dijkstra Algorithm (En Kısa Yol)
**Tanım:** Kenar ağırlıkları (weight) olan bir grafta, başlangıç düğümünden diğer tüm düğümlere olan en kısa yolu bulur. "Greedy" (Açgözlü) bir yaklaşım kullanır; her adımda ulaşabildiği en yakın düğümü seçer.

* **Püf Nokta:** Negatif kenar ağırlıklarıyla çalışmaz (Onun için Bellman-Ford gerekir).
* **Veri Yapısı:** Priority Queue (Min-Heap).

### Karmaşıklık Analizi
| Durum | Zaman Karmaşıklığı | Açıklama |
|-------|--------------------|----------|
| **Binary Heap ile** | $O(E \log V)$ | En verimli ve yaygın yöntem. |
| **Array ile** | $O(V^2)$ | Sadece çok yoğun (dense) graflarda mantıklı olabilir. |

> $V$: Düğüm Sayısı, $E$: Kenar Sayısı.
> Google Maps gibi sistemler bu algoritmanın gelişmiş varyasyonlarını (A* gibi) kullanır.

---

## 4. Minimum Spanning Tree (MST) - Prim's Algorithm
**Tanım:** Bir graftaki tüm düğümleri, toplam kenar ağırlığı **en küçük** olacak şekilde birbirine bağlayan ağacı bulur. Döngü (cycle) içermez.
* **Kullanım Alanı:** Elektrik ağı döşeme, bilgisayar ağları, yol planlama.

### Karmaşıklık Analizi
| Algoritma | Zaman Karmaşıklığı | Veri Yapısı |
|-----------|--------------------|-------------|
| **Prim's** | $O(E \log V)$ | Binary Heap (Priority Queue) ile. |

> **Dijkstra ile Farkı:** Dijkstra "A'dan B'ye en kısa yolu" bulur. Prim ise "Tüm noktaları en ucuza bağlamayı" hedefler.