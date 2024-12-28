class StepValueError(ValueError):
    pass

class Iterator:
    def __init__(self, start, stop, step=1 ):
        self.start=start
        self.stop=stop
        if step ==0:
            raise StepValueError('шаг не может быть равен 0')
        self.step = step

    def __iter__(self):
        self.pointer=self.start
        return self

    def __next__(self):
        number=self.pointer
        self.pointer += self.step
        if self.step < 0:
            if self.pointer >= self.stop-1:
                return number
            else:
                raise StopIteration()
        elif self.step > 0:
            if self.pointer <= self.stop+1:
                return number
            else:
                raise StopIteration()

try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')
print()
try:
    iter2 = Iterator(-5, 1)
    for i in iter2:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')
print()
try:
    iter3 = Iterator(6, 15, 2)
    for i in iter3:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')
print()
try:
    iter4 = Iterator(5, 1, -1)
    for i in iter4:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')
print()



