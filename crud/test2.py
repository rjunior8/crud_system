from test import A, B
try:
    from pythoncom import PumpWaitingMessages
    from pythoncom import Empty
    from pythoncom import Missing
    from pythoncom import com_error
    import win32api
except ImportError:
    print("error")

a = A()
b = B()

class C(A, B):
    def __init__(self):
        super(C, self).__init__()
        print(a.s, b.t)
c = C()