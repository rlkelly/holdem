class DefaultDict(object):
    def __init__(self, value):
        self.value = value
        self.dict = {}

    def __add__(self, other):
        if other not in self.dict:
            self.dict[other] = self.value
        else:
            self.dict[other] += 1
        return self

    def __sub__(self, other):
        if other not in self.dict:
            self.dict[other] = -self.value
        else:
            self.dict[other] -= 1
        return self

    def __getitem__(self, other):
        if other not in self.dict:
            self.dict[other] = self.value

    def counter(self):
        lst = []
        for key in self.dict:
            lst.append((key, self.dict[key]))
        return sorted(lst, key=lambda x: (-x[0], x[1]))

    def sorted_values(self):
        return sorted(self.dict.keys())
