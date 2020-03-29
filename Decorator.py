#defined Decorator Function and defined decoratable function as parameter
def Decorator(function):
    def StyleText():
        print('--------------------')
        function()
        print('--------------------')
    return StyleText

def Text():
    print('Give any text that you want to design')

#we can call decorator function these three way
DecObject = Decorator(Text)
DecObject()

#or

Text = Decorator(Text)
Text()

#or

@Decorator
def Text2():
    print('Hello World')

Text2()
