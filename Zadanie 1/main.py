
class FP:
    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.fp = self.check_belongingness()

    def check_belongingness(self):
        if(self.a == self.b):
            return 'fp1'
        elif(self.b == self.c):
            return 'fp2'
        else:
            return 'fp3'

    def calc_line(self, x1, y1, x2, y2, X):
        return (y2-y1)/(x2-x1)*(X-x1) + y1

    def get_value(self, x):
        if(self.fp == 'fp1'):
            return self.calc_line(self.a, 1, self.c, 0, x)
        elif(self.fp == 'fp2'):
            return self.calc_line(self.a, 0, self.b, 1, x)
        elif(self.fp == 'fp3'):
            # wierzchołek
            if(x == self.b):
                return 1
            # lewa część wykresu
            elif(x < self.b):
                return self.calc_line(self.a, 0, self.b, 1, x)
            elif(x > self.b):
                return self.calc_line(self.b, 1, self.c, 0, x)


f = FP(20, 20, 40)
print(f.get_value(33))
