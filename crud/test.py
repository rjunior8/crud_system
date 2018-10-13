class A(object):
    def __init__(self, s = "fjdkjfkd"):
        super(A, self).__init__()
        self.s = s
a = A()

class B(object):
    def __init__(self, t="lsdjk"):
        super(B, self).__init__()
        self.t = t
b = B()

"""class C(A, B):
    def __init__(self):
        super(C, self).__init__()
        print(a.s, b.t)
c = C()"""