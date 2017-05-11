class WeightedQuickUnionUF(object):
    def __init__(self, n):
        self.__count = n
        self.__parent = []
        self.__size = []
        for i in range(n):
            self.__parent.append(i)
            self.__size.append(1)

    def count(self):
        return self.__count

    def find(self, p):
        self.validate(p)
        while self.__parent[p] != p:
            p = self.__parent[p]
        return p

    def validate(self, p):
        self.__n = len(self.__parent)
        if p < 0 or p >= self.__n:
            raise ValueError('index ' + str(p) + ' is not between 0 and ' + str((self.__n-1)))

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        self.__rootP = self.find(p)
        self.__rootQ = self.find(q)
        if self.__rootP == self.__rootQ:
            return

        if self.__size[self.__rootP] < self.__size[self.__rootQ]:
            self.__parent[self.__rootP] = self.__rootQ
            self.__size[self.__rootQ] += self.__size[self.__rootP]
        else:
            self.__parent[self.__rootQ] = self.__rootP
            self.__size[self.__rootP] += self.__size[self.__rootQ]
        self.__count = self.__count - 1

    def test(self):
        print('test')