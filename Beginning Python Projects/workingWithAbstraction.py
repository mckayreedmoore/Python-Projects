from abc import ABC, abstractmethod


#creation of a parent class
class polygon:
    #creation of a normal method
    def shapeCelebrate(self):
        print('Shapes sure are cool!')
    #creation of an abstract method
    @abstractmethod
    def sides(self):
        print('I am a polygon! I have 3 or more sides')
#creation of a child class
class quadrilateral(polygon):
    #modification of the parent class method to fit
        #child class
    def sides(self):
        print('I am a quadrilateral! I have 4 sides')

#instatiation of all classes and methods
shape = polygon()
shape4 = quadrilateral()

shape.sides()
shape.shapeCelebrate()

shape4.sides()
shape4.shapeCelebrate()
