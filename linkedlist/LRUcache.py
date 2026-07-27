class Node:
    def __init__(self,key,value):
        self.key,self.val=key,value
        self.prev=None
        self.next=None
class LRUCache:
    def __init__(self, capacity: int):
        self.cap=capacity
        self.cache={}
        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.next,self.tail.prev=self.tail,self.head

    def remove(self,node):
        prev,nxt=node.prev,node.next
        prev.next=nxt
        nxt.prev=prev
    def insert(self,node):
        prev,nxt=self.head, self.head.next
        node.prev=prev
        node.next=nxt
        self.head.next=node
        nxt.prev=node
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key]=Node(key,value)
        self.insert(self.cache[key])
        if len(self.cache)>self.cap:
            lru=self.tail.prev
            self.remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)