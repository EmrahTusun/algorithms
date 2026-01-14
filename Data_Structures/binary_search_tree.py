class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Ağaca yeni eleman ekler"""
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        if value < current_node.value:
            # Sola git
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_recursive(current_node.left, value)
        else:
            # Sağa git
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_recursive(current_node.right, value)

    def search(self, value):
        """Değer ağaçta var mı kontrol eder"""
        return self._search_recursive(self.root, value)

    def _search_recursive(self, current_node, value):
        if current_node is None:
            return False
        if current_node.value == value:
            return True
        
        if value < current_node.value:
            return self._search_recursive(current_node.left, value)
        else:
            return self._search_recursive(current_node.right, value)

    def inorder_traversal(self, node, result=None):
        """Ağacı küçükten büyüğe sıralı şekilde gezer (Left-Root-Right)"""
        if result is None:
            result = []
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.value)
            self.inorder_traversal(node.right, result)
        return result

# --- TEST ---
if __name__ == "__main__":
    bst = BinarySearchTree()
    # Örnek: 10, 5, 15, 3, 7
    #       10
    #      /  \
    #     5    15
    #    / \
    #   3   7
    
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)
    
    print("Ağaçta 7 var mı?:", bst.search(7))  # True
    print("Ağaçta 20 var mı?:", bst.search(20)) # False
    print("Sıralı Liste:", bst.inorder_traversal(bst.root)) # [3, 5, 7, 10, 15]