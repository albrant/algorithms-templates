# Comment it before submitting
"""
class Node:  
    def __init__(self, value, next_item=None):  
        self.value = value  
        self.next_item = next_item
"""

def solution(node, idx):
    head = node
    current_id = 0
    current_node = node
    previous_node = None
    
    while current_node is not None:
        if current_id == idx:
            # if this is the first node (head)
            if previous_node is not None:
                previous_node.next_item = current_node.next_item
            else:
                head = current_node.next_item
                # we don't have to look any further
                return head
        
        # needed for the next iteration
        previous_node = current_node
        current_node = current_node.next_item
        current_id = current_id + 1
    
    return head

"""
def print_nodes(node):
    while node:
        print(node.value)
        node = node.next_item

def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = solution(node0, 1)
    # result is node0 -> node2 -> node3
    print_nodes(new_head)

test()
"""