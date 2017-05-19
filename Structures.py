class Link:
    """Helper class for the DLList."""

    def __init__(self, item, prev, next):
        self.item = item
        self.prev = prev
        self.next_link = next


class DLList:
    """A doubly-linked list that to be used to implement the Queue."""

    def __init__(self):
        self.list, self.last = None, None
        self.size = 0

    def insert(self, x):
        """Adds x to the front of the DLList"""
        temp_link = Link(x, None, self.list)
        if self.size == 0:
            self.last = temp_link
        else:
            self.list.prev = temp_link
        self.list = temp_link
        self.size += 1

    def remove_last(self):
        if self.size == 0:
            return None
        last = self.last.item
        self.size -= 1
        # Determines if there are any items left. If yes, removes any links to the removed item.
        if self.size > 0:
            self.last = self.last.prev
            self.last.next_link = None
        else:
            self.last = None
            self.list = None
        return last

    def __len__(self):
        return self.size

    def __str__(self):
        """Simple space-delimited string for testing purposes."""
        string = ""
        this = self.list
        while this is not None:
            string += str(this.item) + " "
            this = this.next_link
        return string


class Queue:
    """A Queue class for Breadth First Search."""

    def __init__(self):
        self.list = DLList()

    def enqueue(self, x):
        self.list.insert(x)

    def peek(self):
        if len(self.list) > 0:
            return self.list.last.item

    def dequeue(self):
        return self.list.remove_last()

    def is_empty(self):
        return len(self.list) == 0

    def __len__(self):
        return len(self.list)

class Tree:
    """A very simple tree class for BFS. Assumes all items will be Wikipedia page types."""

    def __init__(self, x, parent=None):
        self.item = x
        self.children = []
        self.parent = parent
        self.visited = False

    def add_children(self, *children):
        for i in children:
            assert isinstance(i, Tree)
            self.children.append(Tree(i, self))

    def links(self):
        return self.item.links

    def title(self):
        return self.item.title

    def num_children(self):
        return len(self.children)

