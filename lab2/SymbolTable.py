class SymbolTable:
    def __init__(self):
        self.root = self.Node()
        self.__pos = 0

    def add(self, key):
        return self.__insert(self.root, key)

    def __insert(self, currentNode, key):
        if currentNode.key is None:
            currentNode.key = key
            currentNode.pos = self.__pos
            self.__pos += 1
            return currentNode.pos
        else:
            if currentNode.key == key:
                return currentNode.pos
            elif currentNode.key > key:
                if currentNode.left is None:
                    currentNode.left = self.Node(key, self.__pos)
                    self.__pos += 1
                    return currentNode.left.pos
                return self.__insert(currentNode.left, key)
            else:
                if currentNode.right is None:
                    currentNode.right = self.Node(key, self.__pos)
                    self.__pos += 1
                    return currentNode.right.pos
                return self.__insert(currentNode.right, key)

    def __str__(self):
        return self.root.display()

    class Node:
        def __init__(self, key=None, pos=None):
            self.left = None
            self.right = None
            self.key = key
            self.pos = pos

        def display(self):
            if self.key is None:
                return ""
            elif self.left is None and self.right is None:
                return str(self.pos) + " " + self.key + "\n"
            elif self.left is None and self.right is not None:
                return str(self.pos) + " " + self.key + "\n" + self.right.display()
            elif self.left is not None and self.right is None:
                return self.left.display() + str(self.pos) + " " + self.key + "\n"
            return self.left.display() + str(self.pos) + " " + self.key + "\n" + self.right.display()
