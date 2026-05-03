class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.hm = {}
        self.numNodes = 0

        #maintain head and tail dummys
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def addToTail(self, node):
        lastNode = self.tail.prev
        lastNode.next = node
        node.prev = lastNode
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.hm:
            #remove current place
            node = self.hm[key]
            self.remove(node)
            self.addToTail(node)
            return node.val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            node = self.hm[key]
            node.val = value
            self.remove(node)
            self.addToTail(node)
        else:
            if self.numNodes >= self.cap:
                #remove least recently used so head
                lru = self.head.next
                self.remove(lru)
                del self.hm[lru.key]
                self.numNodes -= 1
            node = Node(key, value)
            self.hm[key] = node
            self.addToTail(node)
            self.numNodes += 1


