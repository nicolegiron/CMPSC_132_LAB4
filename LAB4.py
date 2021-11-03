# LAB4
#Due Date: 03/06/2021, 11:59PM

"""
### Collaboration Statement:

"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return "Node({})".format(self.value)

    __repr__ = __str__


class SortedLinkedList:
    '''
        >>> x=SortedLinkedList()
        >>> x.add(8.76)
        >>> x.add(1)
        >>> x.add(1)
        >>> x.add(1)
        >>> x.add(5)
        >>> x.add(3)
        >>> x.add(-7.5)
        >>> x.add(4)
        >>> x.add(9.78)
        >>> x.add(4)
        >>> x
        Head:Node(-7.5)
        Tail:Node(9.78)
        List:-7.5 -> 1 -> 1 -> 1 -> 3 -> 4 -> 4 -> 5 -> 8.76 -> 9.78
        >>> x.replicate()
        Head:Node(-7.5)
        Tail:Node(9.78)
        List:-7.5 -> 1 -> 1 -> 1 -> 3 -> 3 -> 3 -> 4 -> 4 -> 4 -> 4 -> 4 -> 4 -> 4 -> 4 -> 5 -> 5 -> 5 -> 5 -> 5 -> 8.76 -> 9.78
        >>> x
        Head:Node(-7.5)
        Tail:Node(9.78)
        List:-7.5 -> 1 -> 1 -> 1 -> 3 -> 4 -> 4 -> 5 -> 8.76 -> 9.78
        >>> x.removeDuplicates()
        >>> x
        Head:Node(-7.5)
        Tail:Node(9.78)
        List:-7.5 -> 1 -> 3 -> 4 -> 5 -> 8.76 -> 9.78
    '''

    def __init__(self):   # You are not allowed to modify the constructor
        self.head=None
        self.tail=None

    def __str__(self):   # You are not allowed to modify this method
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' -> '.join(out)
        return 'Head:{}\nTail:{}\nList:{}'.format(self.head,self.tail,out)

    __repr__=__str__


    def isEmpty(self):
        return self.head == None

    def __len__(self):
        count=0
        current=self.head
        while current:
            current=current.next
            count+=1
        return count


    def add(self, value):
        newNode = Node(value)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        elif value <= self.head.value:
            newNode.next = self.head
            self.head = newNode
        else:
            current = self.head
            while current.next != None and current.next.value < value:
                current = current.next
            if current.next == None:
                self.tail = newNode
            newNode.next = current.next
            current.next = newNode
        return


    def replicate(self):
        newList = SortedLinkedList()
        current = self.head
        zero = False
        if self.isEmpty():
            return None
        else:
            while current != None:
                if type(current.value) == float or current.value < 0:
                    newList.add(current.value)
                elif current.value == 0:
                    if not zero:
                        newList.add(current.value)
                        zero = True
                else:
                    for i in range(current.value):
                        newList.add(current.value)
                current = current.next
            return newList


    def removeDuplicates(self):
        current = self.head
        while current != None and current.next != None:
            if current.next.value == current.value:
                current.next = current.next.next
                if current.next == None:
                    current.tail = current
            else:
                current = current.next
