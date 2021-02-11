class Deque():
    def __init__(self):
        self.array = []
        self.mid = 0

    def push_left(self, val):
        self.array.insert(self.mid, val)

    def push_right(self, val):
        self.array.insert(self.mid, val)

        self.mid = self.mid + 1

    def pop_left(self):
        # If mid is the rightmost element, move it left.
        if self.mid == len(self.array) - 1:
            self.mid = self.mid - 1

        if (len(self.array) > 0):
            return self.array.pop()
        else:
            return None

    def pop_right(self):
        # If the mid is not the leftmost element, move it right.
        if self.mid > 0:
            self.mid = self.mid - 1

        if (len(self.array) > 0):
            return self.array.pop(0)
        else:
            return None

    def peek_left(self):
        if (len(self.array) > 0):
            return self.array[-1]
        else:
            return None

    def peek_right(self):
        if (len(self.array) > 0):
            return self.array[0]
        else:
            return None

    def __str__(self):
        ret = "["

        if len(self.array) == 0:
            return "[]"

        for idx, val in enumerate(self.array):
            if idx == self.mid:
                ret = ret + "({}) ".format(str(val))
            else:
                ret = ret + str(val) + " "

        return ret.strip() + "]"


# Test case
d = Deque()

d.push_left(19)
d.push_left(11)
d.push_left(23)
print(d)

d.push_right(17)
d.push_right(13)
print(d)

d.pop_left()
d.pop_left()
print(d)

d.pop_left()
d.pop_right()
print(d)

# Edge Case where 13 is the only element. Insert 29 left of it.
d.push_right(29)
print(d)

d.push_left(11)
print(d)

d.pop_right()
d.pop_right()
print(d)

# Edge Case where 13 is the only element. Insert 21 right of it.
d.push_left(21)
d.push_left(29)
print(d)

d.push_right(13)
d.push_right(21)
print(d)  # Symmetry!
