class Node:
    def __init__(self, data):
        self.data = data  # Veri
        self.next = None  # Bir sonraki düğüme işaret eden ok (Pointer)

class LinkedList:
    def __init__(self):
        self.head = None  # Listenin başı (Trenin lokomotifi)

    def append(self, data):
        """Listenin sonuna eleman ekler"""
        new_node = Node(data)
        
        # Eğer liste boşsa, yeni eleman baş olur
        if not self.head:
            self.head = new_node
            return
        
        # Değilse, en sona kadar git
        current = self.head
        while current.next:
            current = current.next
        
        # Sonuncunun okunu yeni elemana bağla
        current.next = new_node

    def prepend(self, data):
        """Listenin en başına eleman ekler (Çok Hızlıdır: O(1))"""
        new_node = Node(data)
        new_node.next = self.head  # Yeni eleman eski başı göstersin
        self.head = new_node       # Artık baş (head) yeni eleman olsun

    def delete_value(self, value):
        """Değeri verilen ilk elemanı siler"""
        if not self.head:
            return

        # Eğer silinecek eleman baştaysa
        if self.head.data == value:
            self.head = self.head.next
            return

        # Aradaki bir elemanı silmek için
        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next  # Bağı kopar ve bir sonrakine bağla
                return
            current = current.next

    def print_list(self):
        """Listeyi yazdırır"""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# --- TEST ---
if __name__ == "__main__":
    ll = LinkedList()
    
    ll.append(10)
    ll.append(20)
    ll.append(30)
    print("Liste oluşturuldu:")
    ll.print_list()  # 10 -> 20 -> 30 -> None
    
    ll.prepend(5)
    print("Başa 5 eklendi:")
    ll.print_list()  # 5 -> 10 -> 20 -> 30 -> None
    
    ll.delete_value(20)
    print("20 silindi:")
    ll.print_list()  # 5 -> 10 -> 30 -> None