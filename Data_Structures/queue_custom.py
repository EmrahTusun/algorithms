from collections import deque

class Queue:
    def __init__(self):
        # Deque (Double Ended Queue) başından ve sonundan işlem yapmak O(1)'dir.
        self.items = deque()

    def enqueue(self, item):
        """Kuyruğun sonuna eleman ekler"""
        self.items.append(item)

    def dequeue(self):
        """Kuyruğun başındaki elemanı çıkarır"""
        if not self.is_empty():
            return self.items.popleft() # İşte bu işlem O(1)'dir!
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(list(self.items))

# --- TEST ---
if __name__ == "__main__":
    my_queue = Queue()
    my_queue.enqueue("Müşteri 1")
    my_queue.enqueue("Müşteri 2")
    my_queue.enqueue("Müşteri 3")
    
    print("Queue:", my_queue)            # ['Müşteri 1', 'Müşteri 2', 'Müşteri 3']
    print("Dequeue:", my_queue.dequeue()) # Müşteri 1 (İlk gelen çıktı)
    print("Kalan:", my_queue)            # ['Müşteri 2', 'Müşteri 3']