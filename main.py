ls = []
len_list = int(input("Enter len list "))
while len(ls) < len_list:
    number = int(input("Enter number "))
    ls.append(number)


class WorkWithList:

    def __init__(self, list_: list) -> None:
        self.list_ = list_

    def bubble_sort(self) -> list:
        n = len(self.list_)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.list_[j] > self.list_[j + 1]:
                    self.list_[j], self.list_[j + 1] = self.list_[j + 1], self.list_[j]
        return self.list_

    def sum_list(self) -> int:
        sum_ = 0
        for i in self.list_:
            sum_ += i
        return sum_


l = WorkWithList(ls)

print(l.bubble_sort())
print(l.sum_list())
