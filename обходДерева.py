# Двоичное дерево в Python

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    # Прямой обход дерева
    def traversePreOrder(self):
        print(self.val, end=' ')
        if self.left:
            self.left.traversePreOrder()
        if self.right:
            self.right.traversePreOrder()

    # Центрированный обход дерева
    def traverseInOrder(self):
        if self.left:
            self.left.traverseInOrder()
        print(self.val, end=' ')
        if self.right:
            self.right.traverseInOrder()

    # Обратный обход дерева
    def traversePostOrder(self):
        if self.left:
            self.left.traversePostOrder()
        if self.right:
            self.right.traversePostOrder()
        print(self.val, end=' ')

root = Node(1)

root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

print("Прямой обход дерева: ", end="")
root.traversePreOrder()
print("\nЦентрированный обход дерева: ", end="")
root.traverseInOrder()
print("\nОбратный обход дерева: ", end="")
root.traversePostOrder()