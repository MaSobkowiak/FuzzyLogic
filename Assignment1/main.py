
class FP:
    def __init__(self, a, b, c, x) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.x = x
        self.fp = self.check_belongingness()
        self.y = self.get_value(self.x)

    def check_belongingness(self):
        if(self.a == self.b):
            return 'fp1'
        elif(self.b == self.c):
            return 'fp2'
        else:
            return 'fp3'

    def calc_line(self, x1, y1, x2, y2, X):
        y = (y2-y1)/(x2-x1)*(X-x1) + y1
        if(y > 1):
            return 1
        elif(y < 0):
            return 0
        else:
            return y

    def get_value(self, x):
        if(self.fp == 'fp1'):
            return self.calc_line(self.a, 1, self.c, 0, x)
        elif(self.fp == 'fp2'):
            return self.calc_line(self.a, 0, self.b, 1, x)
        elif(self.fp == 'fp3'):
            # vertex
            if(x == self.b):
                return 1
            # left side
            elif(x < self.b):
                return self.calc_line(self.a, 0, self.b, 1, x)
            # right side
            elif(x > self.b):
                return self.calc_line(self.b, 1, self.c, 0, x)

    def __str__(self) -> str:
        return f'Parameters (a={self.a}, b={self.b}, c={self.c}), fp version is {self.fp}.\n For x={self.x} fp value y={self.y}\n'


# fp1
print(FP(20, 20, 40, 30))
# fp2
print(FP(10, 100, 100, 77))
# fp3
print(FP(10, 30, 40, 13))
