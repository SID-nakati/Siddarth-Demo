class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert_recursive(node.left, key)
        elif key > node.key:
            node.right = self._insert_recursive(node.right, key)
        return node

    def inorder(self):
        self._inorder_recursive(self.root)

    def _inorder_recursive(self, node):
        if node:
            self._inorder_recursive(node.left)
            print(node.key, end="->")
            self._inorder_recursive(node.right)

    def postorder(self):
        self.postorder_recursive(self.root)

    def postorder_recursive(self, node):
        if node:
            self.postorder_recursive(node.left)
        
            self.postorder_recursive(node.right)
            print(node.key, end="->")

    def preorder(self):
        self.preorder_recursive(self.root)

    def preorder_recursive(self, node):
        if node:
            print(node.key, end="->")
            self.preorder_recursive(node.left)
            self.preorder_recursive(node.right)

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)


tree = BST()
tree.insert(50)
tree.insert(30)
tree.insert(70)
tree.insert(20)
tree.insert(40)
tree.insert(60)
tree.insert(80)
tree.insert(45)

tree.inorder()  
print()
tree.postorder()
print()
tree.preorder()

result = tree.search(60)
print("\nFound!" if result else "\nNot Found.")

