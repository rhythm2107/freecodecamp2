class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
    
    def get_picture(self):
        picture = ''

        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            for i in range(self.height):
                picture += f"{'*' * self.width}\n"
    
    def get_amount_inside(self):
        pass

class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        if isinstance(self, Square):
            return f"Square(side={self.width})"
        else:
            return super().__str__()

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.width = height
        self.height = height


# Testing
rect = Rectangle(10, 5)
# print('Area:', rect.get_area())
# print('Perimeter:', rect.get_perimeter())
# rect.set_height(3)
# print('Area:', rect.get_area())
# print('Perimeter:', rect.get_perimeter())
# print(rect)
# print(rect.get_diagonal())
# print(rect.get_picture())
sqr = Square(10)
print(rect)
print(sqr)
sqr.set_side(20)
print(sqr)

# sq = Square(9)
# print(sq.get_area())
# sq.set_side(4)
# print(sq.get_diagonal())
# print(sq)
# print(sq.get_picture())

# rect.set_height(8)
# rect.set_width(16)
# print(rect.get_amount_inside(sq))