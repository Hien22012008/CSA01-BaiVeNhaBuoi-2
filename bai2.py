class MathList:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return str(self.data)

    def __add__(self, other):
        result = [x + other for x in self.data]
        return MathList(result)

    def __sub__(self, other):
        result = [x - other for x in self.data]
        return MathList(result)


m_list = MathList([1, 2, 3, 4, 5])

print(m_list)
m_list += 2
print(m_list.data)
