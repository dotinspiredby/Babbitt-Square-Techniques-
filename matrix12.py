#import sys

class MatrixIntError(Exception):
    def __init__(self, data):
        self.defect = data

    def __str__(self):
        return 'Check your Matrix for unknown data {0}'.format(self.defect)


class MatrixRepError(MatrixIntError):
    def __init__(self, data):
        super().__init__(data)

    def __str__(self):
        return 'Check your Matrix for repetitive data {0}'.format(self.defect)


class MatrixValueError(MatrixIntError):
    def __init__(self, data):
        super().__init__(data)

    def __str__(self):
        return 'Check your Matrix for exceeding "11" values {0}'.format(self.defect)


class TWToneMatrix:
    pc_check = {}

    def __init__(self, data):
        for i in data:
            if not isinstance(i, int):
                raise MatrixIntError(data)
            if i > 11:
                raise MatrixValueError(data)
            if i in TWToneMatrix.pc_check:
                raise MatrixRepError(data)
            else:
                TWToneMatrix.pc_check[i] = TWToneMatrix.pc_check.get(i, 0) + 1
            TWToneMatrix.pc_check.clear()

        self.__P0 = data
        self.__dist = data[0]
        self.__full = [[(j - i + 12 + self.__dist) % 12 for j in self.__P0] for i in self.__P0]

    def __str__(self):
        return '\t'.join(map(str, self.__P0))

    def __reversed__(self):
        return '\t'.join(map(str, self.__P0[::-1]))

    def full(self):
        """Returns the full Babbitt Square"""
        return '\n'.join(['\t'.join(map(str, item)) for item in self.__full])

    def prime(self, index):
        """Returns prime by index of transposition"""
        prime = [(i + index) % 12 for i in self.__P0]
        return TWToneMatrix(prime)

    def retrograde(self, index=0):
        """Returns prime backwards right to the left"""
        retr = self.prime(index=index).__reversed__()
        return retr

    def inversion(self, index=0):
        """Returns columns from Babbitt Square"""
        i = [(j[0]+index) % 12 for j in self.__full]
        return TWToneMatrix(i)

    def retrogradeinversion(self, index=0):
        """Returns columns upside-down"""
        retrinv = self.inversion(index=index).__reversed__()
        return retrinv

#Example: m = TWToneMatrix([_,_,_,_,...])


#m = TWToneMatrix([5, 7, 1, 2, 0, 9, 10, 8, 4, 6, 3, 11])
#n = TWToneMatrix([5, 7, 1, 2, 0, 9, 10, 'm', 4, 6, 3, 11])
#k = TWToneMatrix([5, 7, 1, 2, 0, 9, 10, 4, 4, 6, 3, 11])
#o = TWToneMatrix([5, 7, 1, 2, 0, 9, 10, 18, 4, 6, 3, 11])
#m = TWToneMatrix(list(map(int, sys.argv[1::])))

#print(m)
#print(m.full())
#print(m.prime(3))
#print(m.inversion(4))
#print(m.retrograde(3))
#print(m.retrogradeinversion(8))


