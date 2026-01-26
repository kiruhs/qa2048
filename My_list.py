#  [3,4,5] -- <<1, 3, 4>>

class My_arr(list):
    """This class is some new type of list with crazy functions inside
    it may be a list of numbers only, booleans are OK
    all elements should be sorted ascended automatically"""

    def __init__(self, it):
        it = list(it)
        for i in it:
            if not isinstance(i, (int, float, bool)):
                raise NotImplementedError
        super().__init__(sorted(it))

    def __str__(self):
        return f"<<{', '.join(str(item) for item in self)}>>"

    def append(self, __object):
        if not isinstance(__object, (int, float, bool)):
            raise NotImplementedError
        super().append(__object)
        self.sort()

    def __len__(self):
        cnt = 0
        for i in self:
            if i >= 0:
                cnt += 1
        return cnt

    @property
    def dif(self):
        return self[-1] - self[0]

    @property
    def length(self):
        return super().__len__()

    @property
    def even(self):
        return My_arr([i for i in self if i%2 == 0])

    def __add__(self, other):
        if isinstance(other, (My_arr, list)):
            return My_arr(super().__add__(other))

    def __sub__(self, other):
        if not isinstance(other, int) or other < 0:
            raise TypeError("Can work with non-negative integer only")

        if other > self.length:
            print("The number is greater than list length")
            return None

        for _ in range(other):
            self.pop()
        return self

    def __eq__(self, other):
        if sum(self) == sum(other):
            return True
        return False
# dunder methods - Magic methods
    def __gt__(self, other):
        if sum(self) > sum(other):
            return True
        return False


ls = My_arr([3,-6,4, 15,0, 9])
ls1 = My_arr([3,-4,1, 15,0, 9, -100])
ls2 = My_arr([0, -7, 12, 0, -4])
ls3 = [10, -10, -40, 2]
ls.append(-100)
# ls.length()  len(list)
print(ls)
print(ls[2:5])
print(len(ls)) # I want the len function includes only non-negative values
# print(ls.dif)
# print(ls.length)
# print(ls.even)
# print(ls.length)
ll = ls + ls3 + ls2
print(ll)
print(ll - 11)
print(ls > ls1 > ls2)