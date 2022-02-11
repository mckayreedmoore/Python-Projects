
mySentence = 'loves the color '

colorList = ['blue','orange','green', 'yellow', 'red', 'pink']


def colorFunction(name):
    lst = []
    for i in colorList:
        msg = '{0} {1}{2}'.format(name,mySentence,i)
        lst.append(msg)
    return lst
    
def getName():
    go = True
    while go:
        name = input('What is your name?')
        if name == '':
            print('You need to provide a name.')
        elif name == 'Sally':
            print('You can not use this software sally')
        else:
            go = False
    lst = colorFunction(name)
    for i in lst:
        print(i)
getName()


mittens = True
def haveMittens():
    if mittens:
        print('congrats! you have mittens')
    else:
        print('sorry, no mittens for you')
haveMittens()
    
