class Element(object):
    """docstring for Linked List Element."""
    def __init__(self, value):
        self.value = value
        self.next  = None

class LinkedList(object):
    """docstring for LinkedList."""
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        element = None;
        current = self.head
        while position > 0:
            element = current
            current = current.next
            position -= 1
        return element

    def insert(self, new_element, position):
        current = self.head
        if(position == 1):
            new_element.next = current
            self.head = new_element
        else:
            while (position - 2) > 0:
                current = current.next
                position -= 1
            new_element.next = current.next
            current.next = new_element

    def delete(self, value):
        current = self.head
        if(current.value == value):
            self.head = current.next
        else:
            while current.next:
                if(current.next.value == value):
                    current.next = current.next.next
                current = current.next


e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print ll.head.next.next.value
# Should also print 3
print ll.get_position(3).value

# Test insert
ll.insert(e4,3)
# Should print 4 now
print ll.get_position(3).value

# Test delete
ll.delete(1)
# Should print 2 now
print ll.get_position(1).value
# Should print 4 now
print ll.get_position(2).value
# Should print 3 now
print ll.get_position(3).value
