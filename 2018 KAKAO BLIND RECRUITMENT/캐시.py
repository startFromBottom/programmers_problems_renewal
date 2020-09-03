"""

problem link : https://programmers.co.kr/learn/courses/30/lessons/17680?language=python3

"""


class Node:
    """
    Doubly Linked List

    """

    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None


class LRUCache:
    """
    put, get Time Complexity : O(1)

    """

    def __init__(self, size: int):
        self.capacity = size
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add(self, node: Node) -> None:
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail

    def _remove(self, node: Node) -> None:
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def get(self, city: str) -> int:
        """
        cache에 존재 -> cache hit : return 1
        cache에 존재 x -> cache miss : return 5
        """
        if city in self.cache:
            cur_node = self.cache[city]
            self._remove(cur_node)
            self._add(cur_node)
            return 1
        return 5

    def put(self, city: str, t: int) -> None:
        if city in self.cache:
            self._remove(self.cache[city])
        cur_node = Node(city, t)
        self._add(cur_node)
        self.cache[city] = cur_node
        if len(self.cache) > self.capacity:
            node = self.head.next
            self._remove(node)
            del self.cache[node.key]


def solution(cacheSize, cities):
    time = 0
    cache = LRUCache(size=cacheSize)
    for t, city in enumerate(cities):
        city = city.lower()
        time += cache.get(city)
        cache.put(city, t)

    return time
