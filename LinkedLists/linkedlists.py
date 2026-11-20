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

    def insert(self, d, idx):
        n = Node(d)

        curr = self.root
        curr_idx = 0

        for i in range(idx - 1):
            if curr != None:
                curr = curr.get_next()

        temp = curr.get_next()
        curr.set_next(n);
        n.set_next(temp)
        self.size = self.size + 1

def from_list(lst):
    l = None
    for i in lst:
        if l is None:
            n = Node(i)
            l = LinkedLists(n)
        else:
            l.add_to_end(i)
    return l
        

def main():
    r = Node(2)

    l = LinkedLists(r)
    l.add_to_end(5)
    l.add_to_end(7)

    print(f"Size:{l.get_size()}")

    l.print_all()

    lst_new = [20, 50, 70, 90]
    new_ll = from_list(lst_new)
    new_ll.print_all()

main()