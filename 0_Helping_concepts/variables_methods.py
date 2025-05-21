# Variables
"""
4 types of Variables
- Global Variable
- Local Variable
- Instance Object Variable
- Class Object Variable (static Variables)
"""
# Creation + Access
class Test:          # Test is a Global Variable
    x = 1            # x is a class Object (static) Variable
    def f1(self, g): # f1 is also a variable that represents the function object
        self.a = g   # self is a local variable | self.a is an instance object variable | g is a local variable
t1 = Test()          # t1 is a global variable
# --------------------------------------------------------------------------
# methods
"""
4 types of methods
- instance method
- static method
- class method
- non-member functions
(Jo function kisi class main bn raha ha wo member function ho ga | instance + static + class)
(Jo function kisi class main nahi bn raha ha wo non-member function ho ga)
"""
class SecondTest:
    def f1(self):   # instance method/instance object method | minimum 1 argument required
        self.a = 15
        SecondTest.x1 = "we can access/create class object variable from any where"
    @staticmethod   # static method kisi object k liay specifically kam nahi krta. but class main kuch na kuch kr raha hota ha
    def f2():       #
        SecondTest.x5 = 5 # define another class object variable from static method
        pass
    @classmethod    #
    def f3(cls):    #
        cls.x4 = 4  #
        SecondTest.x5 = 5 # define another class object variable from cls object method
        pass

def func():
    print("Non member function")


st1 = SecondTest()
st1.c = 3
print(st1.c)
# print(st1.a) # it will give an error. as at that time a is not in an instance object variable
st1.f1() # f1(st1)
print(st1.a)
SecondTest.x6 = 6 # define another class object variable from outside the class