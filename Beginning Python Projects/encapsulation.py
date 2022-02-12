class encapDemo:
    #here is a demo of using underscore prefixes to
    #show the state of a variable
    _protectedVar = 10
    __privateVar = 20

    def getPrivate(self):
        print(self.__privateVar)

demo = encapDemo()

print(demo._protectedVar)
demo.getPrivate()
    
