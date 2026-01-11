from collections import defaultdict, deque

class Graph:
    def __init__(self):
        # Grafı tutmak için "adjacency list" (komşuluk listesi) kullanıyoruz
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        """İki düğüm arasına kenar ekler (Yönlü graf)"""
        self.graph[u].append(v)

    def bfs(self, start_node):
        """Breadth First Search (Genişlik Öncelikli Arama)"""
        visited = set()
        queue = deque([start_node])
        visited.add(start_node)
        
        result = []

        while queue:
            # Kuyruğun başından bir eleman al
            vertex = queue.popleft()
            result.append(vertex)

            # O düğümün komşularını gez
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return result

    def dfs(self, start_node):
        """Depth First Search (Derinlik Öncelikli Arama)"""
        visited = set()
        result = []
        
        def _dfs_recursive(vertex):
            visited.add(vertex)
            result.append(vertex)
            
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    _dfs_recursive(neighbor)
        
        _dfs_recursive(start_node)
        return result

# --- TEST KISMI ---
if __name__ == "__main__":
    g = Graph()
    # Örnek Graf Oluşturma:
    # 0 -> 1, 0 -> 2
    # 1 -> 2
    # 2 -> 0, 2 -> 3
    # 3 -> 3
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print("BFS Sonucu (0'dan başla):", g.bfs(2))
    print("DFS Sonucu (2'den başla):", g.dfs(2))