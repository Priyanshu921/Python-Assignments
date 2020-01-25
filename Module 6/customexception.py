class MyError(Exception):
    def __init__(self,value):
        self.value=value
    def __str__(self):
        return(repr(self.value))
try:
    raise(MyError(2*3))
except MyError as er:
    print("A new Exception Occured",er.value)
