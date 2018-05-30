#Node class
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

#Linkenlist Class
class Linkenlist:

    def __init__(self):
        self.head = None

    def printlist(self):
        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.next
# Code execution

if __name__=='__main__':

    llist = Linkenlist()
    llist.head = Node(1)

    second = Node(2)
    third = Node(3)

    llist.head.next = second
    second.next =third
    # print list
    llist.printlist()