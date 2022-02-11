

def getValues ():
    var1 = input('Please enter your first number: ')
    var2 = input('Please enter your second number: ')
    multiplyTime(var1,var2)

def multiplyTime (var1,var2):
    go = True
    while go:
        try:
            x = int(var1)
            y = int(var2)
            z = x * y
            go = False
        except:
            print('\n It looks like you did not type in numeric values. Try again. \n')
            getValues()
            
            
    print('{} * {} = {}'.format(x,y,z))
    return

getValues()
