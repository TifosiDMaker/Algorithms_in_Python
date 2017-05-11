import bookcode.WeightedQuickUnionUF as uf
from random import randint
import numpy
import math
import time


class Percolation(object):
    def __init__(self, n):
        self.__n = n
        self.__maxRow = n
        self.__maxCol = n
        self.__isOpen = []
        self.__openNum = 0
        for i in range(n * n):
            self.__isOpen.append(0)
        self.__wq = uf.WeightedQuickUnionUF(n * n + 2)

    def open(self, row, col):
        self.__site = self.convert(row, col)
        if not self.isOpen(row, col):
            self.__openNum += 1
            self.__isOpen[self.__site] = 1
            if self.__site < self.__n:
                self.__wq.union(self.__site, self.__n * self.__n)
            elif self.__site >= self.__n * (self.__n - 1):
                self.__wq.union(self.__site, self.__n * self.__n + 1)
            for dot in self.surrounding(row, col):
                if dot >= 0 and dot < self.__n * self.__n and self.__isOpen[dot] == 1:
                    self.__wq.union(self.__site, dot)

    def isOpen(self, *num):
        if len(num) == 1:
            return self.__isOpen[num[0]] == 1
        elif len(num) == 2:
            return self.__isOpen[self.convert(num[0], num[1])] == 1

    def isFull(self, row, col):
        self.__tempsite = self.convert(row, col)
        return self.__wq.connected(self.__tempsite, self.__n * self.__n)

    def numberOfOpenSites(self):
        return self.__openNum

    def percolates(self):
        self.__temp = self.__n * self.__n
        return self.__wq.connected(self.__temp, self.__temp + 1)

    def convert(self, row, col):
        if row > 0 and col > 0:
            return (row - 1) * self.__n + col - 1
        else:
            return -1

    def surrounding(self, row, col):
        self.__surrounding = []

        self.__surrounding.append(self.convert(row, col - 1))
        self.__surrounding.append(self.convert(row + 1, col))
        self.__surrounding.append(self.convert(row, col + 1))
        self.__surrounding.append(self.convert(row - 1, col))

        return self.__surrounding


class PercolationStats(object):
    def __init__(self, n, t):
        self.start = time.time()
        self.totalTime = []
        for tttime in range(t):
            self.__per = Percolation(n)
            self.__time = 0
            for i in range(n - 1):
                self.__p = randint(1, n)
                self.__q = randint(1, n)
                if not self.__per.isOpen(self.__p, self.__q):
                    self.__per.open(self.__p, self.__q)
                    self.__time += 1
            while not self.__per.percolates():
                self.__p = randint(1, n)
                self.__q = randint(1, n)
                if not self.__per.isOpen(self.__p, self.__q):
                    self.__per.open(self.__p, self.__q)
                    self.__time += 1
            self.totalTime.append(self.__time / (n * n))
        print(time.time() - self.start)
        #print("mean                    = " + str(self.mean()))
        #print("stddev                  = " + str(self.stddev()))
        #print("95% confidence interval = [" + str(self.confidenceLo()) + ", " + str(self.confidentceHi()) + "]")

    def mean(self):
        return numpy.mean(self.totalTime)

    def stddev(self):
        return numpy.std(self.totalTime)

    def confidenceLo(self):
        return self.mean() - (1.96 * math.sqrt(self.stddev()) / math.sqrt(len(self.totalTime)))

    def confidentceHi(self):
        return self.mean() + (1.96 * math.sqrt(self.stddev()) / math.sqrt(len(self.totalTime)))
