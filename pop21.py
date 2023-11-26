class NonPositiveError(Exception):
    pass


class PositiveList(list):
    def append(self, el):
        if el <= 0:
            raise (NonPositiveError)
        else:
            super().append(el)


m = PositiveList()
m.append(1)
m.append(0)
m.append(-1)
print(m)
