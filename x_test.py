class Test:
    def test01(self):
        self.a=1
        self.b=2
    def sum(self):
        print(self.a+self.b)

sum1 = Test()
sum1.test01()
sum1.sum()