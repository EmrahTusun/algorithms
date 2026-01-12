class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Yığının en üstüne eleman ekler"""
        self.items.append(item)

    def pop(self):
        """En üstteki elemanı çıkarır ve döndürür"""
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        """En üstteki elemana bakar (çıkarmaz)"""
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

# --- TEST ---
if __name__ == "__main__":
    my_stack = Stack()
    my_stack.push("Kitap 1")
    my_stack.push("Kitap 2")
    my_stack.push("Kitap 3")
    
    print("Stack:", my_stack)          # ['Kitap 1', 'Kitap 2', 'Kitap 3']
    print("Pop:", my_stack.pop())      # Kitap 3 (En son gelen çıktı)
    print("Peek:", my_stack.peek())    # Kitap 2 (Şu an en üstteki)