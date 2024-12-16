class Unique(object):
    def __init__(self, items, **kwargs):
        self.i = 0
        ignore_case = False
        if 'ignore_case' in kwargs:
            ignore_case = kwargs['ignore_case']
        self.data = []
        for elem in items:
            if ignore_case:
                if elem not in self.data:
                    self.data.append(elem)
            else:
                if (isinstance(elem, str) and elem.lower() not in [str(i).lower() for i in self.data]) or (not isinstance(elem, str) and elem not in self.data):
                    self.data.append(elem)

    def __next__(self):
        self.i += 1

    def __iter__(self):
        return self.data[self.i]


if __name__ == "__main__":
    a = Unique([1, 2, 2, 2, 1, 0, 4, 2, 'bb', 'bd', 'Bd', 'DD'], ignore_case=True)
    print(a.data)

    from gen_random import gen_random
    b = Unique(gen_random(10, 1, 3))
    print(b.data)
