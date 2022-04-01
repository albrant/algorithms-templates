# Comment it before submitting
"""
class Node:  
    def __init__(self, value, next_item=None):  
        self.value = value  
        self.next_item = next_item
"""

def solution(node, elem) -> int:
    idx = -1
    while node:
        idx += 1
        if node.value == elem:
            return idx
        node = node.next_item
    return -1
"""
def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    idx = solution(node0, "node2")
    print(idx)
    # result is idx == 2
test()
"""