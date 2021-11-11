class ATM (object):
        def __init__(self,pinno,accno):
            self.pinno=pinno
            self.accno=accno
        def start(self):
            print("welcome")
        def end(self):
            print("vacation")

bank1= ATM ("1123","77669645098267915")
print(bank1.pinno)
print(bank1.accno)
print(bank1.start())