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
        return picture
    
    def get_amount_inside(self, shape):
        column = self.width // shape.width
        row = self.height // shape.height
        count = column * row
        return count

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

    # Definining aliases for same method
    set_height = set_width = set_side


# Testing
rect = Rectangle(4, 8)
sqr = Square(12)
rect.get_amount_inside(sqr)
sqr.get_amount_inside(rect)