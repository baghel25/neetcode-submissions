
class MinStack:

    def __init__(self):
        self.array = []
        self.minimum = float('inf')

    def push(self, val: int) -> None:
        if len(self.array) == 0:
            self.minimum = val
        elif val <= self.minimum:
            self.minimum = val

        self.array.append(val)

    def pop(self) -> None:
        if self.array != []:
            last_val = self.array[-1]
            self.array.pop()

            if last_val <= self.minimum:
                self.minimum = float('inf')

                for elm in self.array:
                    self.minimum = min(elm, self.minimum)

    def top(self) -> int:
        return self.array[-1]

    def getMin(self) -> int:
        return self.minimum
