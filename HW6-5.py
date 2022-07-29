class Stationary:
    def __init__(self,tittle="Something that can draw"):
        self.tittle = tittle

    def draw(self):
        print(f"Just star drawing! {self.tittle}")

class Pen(Stationary):
    def draw(self):
        print(f'Just start drawing with pen! {self.tittle}')

class Pencil(Stationary):
    def draw(self):
        print(f'Just start drawing with Pencil! {self.tittle}')

class Marker(Stationary):
    def draw(self):
        print(f'Just start Drawing with Market')

stat = Stationary()
stat.draw

mark = Marker()
pen = Pencil()

mark.draw()
pen.draw()