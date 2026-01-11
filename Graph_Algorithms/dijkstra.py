import heapq

def dijkstra(graph, start):
    """
    Dijkstra's Shortest Path Algorithm
    graph: {düğüm: {komşu: ağırlık, ...}, ...}
    start: Başlangıç düğümü
    """
    # Mesafeleri sonsuz başlat, başlangıcı 0 yap
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    
    # Öncelik kuyruğu (mesafe, düğüm) tutar
    # Başlangıç noktasını kuyruğa ekle
    pq = [(0, start)]
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        # Eğer kuyruktan gelen mesafe, bildiğimizden büyükse atla (Gereksiz işlem)
        if current_distance > distances[current_node]:
            continue
        
        # Komşuları gez
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Daha kısa bir yol bulduysak güncelle
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
                
    return distances

# --- TEST ---
if __name__ == "__main__":
    # Graf yapısı (Sözlük içinde sözlük)
    # A -> B (1), A -> C (4)
    # B -> C (2), B -> D (5)
    # C -> D (1)
    # D -> (bitiş)
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'C': 2, 'D': 5},
        'C': {'D': 1},
        'D': {}
    }
    
    start_node = 'A'
    shortest_paths = dijkstra(graph, start_node)
    
    print(f"Başlangıç düğümü '{start_node}' için en kısa mesafeler:")
    for node, dist in shortest_paths.items():
        print(f"Node {node}: {dist}")