import heapq

def prim_mst(graph, start_node):
    """
    Prim's Algorithm for Minimum Spanning Tree (MST)
    Tüm düğümleri en az maliyetle birbirine bağlar.
    """
    mst_cost = 0
    visited = set()
    
    # Priority Queue: (maliyet, düğüm, geldiği_düğüm)
    # Başlangıç düğümünün maliyeti 0, geldiği yer None
    pq = [(0, start_node, None)]
    mst_edges = []

    while pq:
        cost, current_node, prev_node = heapq.heappop(pq)

        if current_node in visited:
            continue

        visited.add(current_node)
        mst_cost += cost
        
        # Eğer bir yerden geldiysek (başlangıç değilse), o kenarı kaydet
        if prev_node is not None:
            mst_edges.append((prev_node, current_node, cost))

        # Komşuları gez
        for neighbor, weight in graph[current_node].items():
            if neighbor not in visited:
                heapq.heappush(pq, (weight, neighbor, current_node))

    return mst_cost, mst_edges

# --- TEST ---
if __name__ == "__main__":
    # Örnek Graf (Dijkstra'daki gibi)
    # A --1--> B
    # A --4--> C
    # B --2--> C
    # B --5--> D
    # C --1--> D
    # Graf yön süz (Undirected) olduğu için iki taraflı ekliyoruz
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    
    total_cost, edges = prim_mst(graph, 'A')
    
    print(f"MST Toplam Maliyet: {total_cost}")
    print("MST Kenarları:")
    for u, v, w in edges:
        print(f"{u} - {v} (Ağırlık: {w})")