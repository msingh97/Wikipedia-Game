class Link:
    """Helper class for the DLList."""

    def __init__(self, item, prev, next):
        self.item = item
        self.prev_link = prev
        self.next_link = next


class DLList:
    """A doubly-linked list that to be used to implement the Queue."""

    def __init__(self):
        self.front, self.end = None, None
        self.size = 0

    def insert(self, x):
        """Insert x into the front of the DLList."""
        self.front = Link(x, None, self.front)
        if self.is_empty():
            self.end = self.front
        self.size += 1

    def remove_last(self):
        """Removes and returns the end of the DLList."""
        assert self.size > 0
        last_item = self.end.item
        self.end = self.end.prev_link
        self.end.next_link = None
        self.size -= 1
        return last_item

    def peek(self):
        """Returns the last item without removing it."""
        return self.end.item

    def is_empty(self):
        return self.size == 0

    def __str__(self):
        string = "["
        current = self.front
        while current != None:
            string += str(current.item) + ", "
        string += "]"
        return string


class Queue:
    """Queue class, uses a doubly-linked list for ordering."""

    def __init__(self):
        self.ordered_list = DLList()

    def enqueue(self, x):
        """Add item x to the queue."""
        self.ordered_list.insert(x)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.ordered_list.remove_last()

    def size(self):
        return self.ordered_list.size

    def is_empty(self):
        return self.ordered_list.is_empty()