class TrieNode:
    def __init__(self):
        self.children = {} # Harfleri tutan sözlük (Örn: 'a': Node, 'b': Node)
        self.is_end_of_word = False # Kelime burada bitiyor mu?

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """Kelimeyi ağaca ekler"""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        """Kelime ağaçta tam olarak var mı? (Örn: 'elm' ararsan 'elma' varsa False döner)"""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        """Bu önek ile başlayan kelime var mı? (Autocomplete mantığı)"""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# --- TEST ---
if __name__ == "__main__":
    trie = Trie()
    
    words = ["apple", "app", "application", "bat", "batman"]
    for w in words:
        trie.insert(w)
    
    print("Sözlük Yüklendi:", words)
    print("-" * 30)
    
    print("'app' var mı?", trie.search("app"))      # True
    print("'appl' var mı?", trie.search("appl"))    # False (Tam kelime değil)
    
    print("'bat' ile başlayan var mı?", trie.starts_with("bat")) # True
    print("'z' ile başlayan var mı?", trie.starts_with("z"))     # False