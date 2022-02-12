
class polygon:
    def sides(shelf):
        print('I am a polygon! I have 3 or more sides')
    def shapeCelebrate(self):
        print('Shapes sure are cool!')

class quadrilateral(polygon):
    def sides(self):
        print('I am a quadrilateral! I have 4 sides')

shape = polygon()
shape4 = quadrilateral()

shape.sides()
shape.shapeCelebrate()

shape4.sides()
shape4.shapeCelebrate()
