class A:
    def __init__(self,a,b):
        self.a1=a
        self.b1=b
class B:
    def printa(self):
        print("hii")
class C(B,A):
    def g(self):
        print("hello")
o2=C(2,3)
print(o2.a1,o2.b1)
o2.printa()
o2.g()