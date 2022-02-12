class encapDemo:
    #here is a demo of using underscore prefixes to
    #show the state of a variable
    _protectedVar = 10
    __privateVar = 20

    #creates a method that is able to access the
    
    def getPrivate(self):
        print(self.__privateVar)

demo = encapDemo()

print(demo._protectedVar)
demo.getPrivate()
    
