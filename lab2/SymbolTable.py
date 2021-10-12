class SymbolTable:
    def __init__(self):
        self.root = None
        self.__pos = 0

    def add(self, key):
        if self.root is None:
            self.root = self.Node(key, self.__pos)
            self.__pos += 1
            return self.root.pos

        node = self.__insert(self.root, key)
        return node.pos

    def __insert(self, currentNode, key):
        if currentNode is None:
            currentNode = self.Node(key, self.__pos)
            self.__pos += 1
            return currentNode
        else:
            if currentNode.key == key:
                return currentNode
            elif currentNode.key > key:
                currentNode.left = self.__insert(currentNode.left, key)
                return currentNode.left
            else:
                currentNode.right = self.__insert(currentNode.right, key)
                return currentNode.right

    class Node:
        def __init__(self, key, pos):
            self.left = None
            self.right = None
            self.key = key
            self.pos = pos
