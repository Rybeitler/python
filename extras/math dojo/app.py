class Math_dojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num
        for x in nums:
            self.result += x
        return self

    def subtract(self, num, *nums):
        self.result -= num
        for x in nums:
            self.result-=x
        return self
    def __repr__(self):
        return f"{self.result}"
md = Math_dojo()

test1 = md.add(2,2,5).subtract(1, 1, 3).add(10, 10, 5).subtract(5, 5, 5,).subtract(3, 3).add(1,1,1,1,1,1,1,1,1)
print(test1)