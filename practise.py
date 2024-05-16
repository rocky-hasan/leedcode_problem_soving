# list1=[1,2,3,1,2,3,1,4,4]
# # output=[1,2,3,'_','_','_' ]
# v=sorted(list1)
# print(v)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def insertAtBegin(self, head):
        new_node = Node(head)
        if self.next is None:
            self.next = new_node
        else:
            new_node.next = self.next
            self.next = new_node
        def insertAny(self,head,index):
            new_node=Node(head)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3

node1.insertAtBegin(0)

current = node1
while current:
    print(current.data)
    current = current.next