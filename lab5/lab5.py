from random import randint

class Book:

    title = "1984"
    author = "George Orwell"
    year = 1946

    # def __init__(self, title, author, year):
    #     self.title = title
    #     self.author = author
    #     self.year = year


    def get_info(self) -> str:
        return f"Title of the book: {self.title}, Author: {self.author}, Year of publishing: {self.year}"


class Circle:

    center: tuple[float, float]
    radius: float

    def __init__(self, radius, center=(0,0)):
        self.radius = radius
        self.center = center


    def get_radius(self) -> float:
        return self.radius


    def set_radius(self, new_radius):
        self.radius = new_radius


class Game:

    status : bool

    def __init__(self):
        self.status = False

    def play(self):
        self.status = bool(randint(0, 1))
        return "win" if self.status else "lost"



if __name__ == "__main__":
    c = Circle(3)
    c.set_radius(5)
    print(c.get_radius())