class Easylist:
    lst = []

    def _binary_search(self, s, e, v):
        if s > e:
            return False
        
        m = s + e // 2

        if self.lst[m] == v:
            return True
        elif self.lst[m] < v:
            return self._binary_search(m + 1, e, v)
        elif self.lst[m] > v:
            return self._binary_search(s, m - 1, v)

    def _lst_sort(self):
        for l in range(len(self.lst)):
            for n in range(l + 1, len(self.lst)):
                if self.lst[l] > self.lst[n]:
                    temp = self.lst[l]
                    self.lst[l] = self.lst[n]
                    self.lst[n] = temp

    def is_present(self, v):
        self._lst_sort()
        return self._binary_search(0, len(self.lst)-1, v)

    def add_number(self, n):
        self.lst.append(n)

    def delete_number(self, n):
        self.lst.remove(n)

def main():

    l = Easylist()
    l.add_number(3)
    l.add_number(10)
    l.add_number(1)

    print(l.is_present(3)) # True
    print(l.is_present(20)) # False

    l.delete_number(3)
    print(l.is_present(3)) # False


main()