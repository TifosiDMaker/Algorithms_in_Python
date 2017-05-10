class WeightedQuickUnionUF(object):
    def __init__(self, n):
        self.__count = n
        self.__parent = []
        self.__size = []
        for 