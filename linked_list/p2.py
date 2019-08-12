'''
P2. Remove duplicates from a linked list

8/11/19
Update: Changed Level of "prevous = node" to the else statment 
This handles the case where multiple nodes are the same right after each other
'''


import p1

class Node(p1.Node):
    def remove_duplicates(self):
        els = []
        node = self
        previous = None
        while node != None:
            if node.val in els:
                print(f"Value Is a duplicate {node.val}")
                previous.next = node.next
            else:
                els.append(node.val)
                previous = node
            node = node.next

if __name__ == "__main__":

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(2)
    node4 = Node(2)
    node5 = Node(3)
    node6 = Node(1)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6

    node1.remove_duplicates()
    node1.traverse()
