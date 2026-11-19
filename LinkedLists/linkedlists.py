class Node(object):
    d = 0
    n = None

    def __init__(self, d):
        self.d = d
        self.n = None

    def get_data(self):
        return self.d

    def set_data(self, d):
        self.d = d

    def get_next(self):
        return self.n

    def set_next(self, n):
        self.n = n

class LinkedLists(object):
    root = None
    size = 0

    def __init__(self, root):
        self.root = root
        self.size = 1

    def get_size(self):
        return self.size

    def print_all(self):
        curr = self.root
        while curr != None:
            print(curr.get_data())
            curr = curr.get_next()

    def add_to_end(self, d):
        n = Node(d)

        curr = self.root
        while curr.get_next() != None:
            curr = curr.get_next()
        curr.set_next(n)
        self.size = self.size + 1

def main():
    r = Node(2)

    l = LinkedLists(r)
    l.add_to_end(5)
    l.add_to_end(7)

    print(l.get_size())

    l.print_all()

main()