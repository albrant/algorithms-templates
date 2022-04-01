# Comment it before submitting
"""
class DoubleConnectedNode:  
    def __init__(self, value, next=None, prev=None):  
        self.value = value  
        self.next = next  
        self.prev = prev
"""

def solution(node):
    p = node
    q = p.next
    p.next = None
    p.prev = q
    while q is not None:
        q.prev = q.next
        q.next = p
        p = q
        q = q.prev
    return p

"""
def print_nodes(node: DoubleConnectedNode) -> None:
    while node:
        print(node.value, '(', end='')
        if node.prev is not None:
            print('prev = ',node.prev.value, ', ', end='')
        if node.next is not None:
            print('next = ',node.next.value, end='')
        else: print('next = None', end='')
        print(')')
        node = node.next


def test():
    node3 = DoubleConnectedNode("node3")
    node2 = DoubleConnectedNode("node2")
    node1 = DoubleConnectedNode("node1")
    node0 = DoubleConnectedNode("node0")

    node0.next = node1

    node1.prev = node0
    node1.next = node2

    node2.prev = node1
    node2.next = node3

    node3.prev = node2

    print_nodes(node0)
    new_head = solution(node0)
    print()
    print_nodes(new_head)
    

test()
"""
    # result is 
    # new_head == node3
    # node3.next == node2
    # node2.next == node1 node2.prev == node3
    # node1.next == node0 node1.prev == node2
    # node0.prev == node1