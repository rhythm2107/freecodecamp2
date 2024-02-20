import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):

        if not kwargs:
            raise ValueError("You need to pass at least one argument to the function.")
        
        # Initialize two lists for operations below
        self.unpack = []
        self.contents = []

        # Unpack kwargs dict into list of lists
        for key, val in kwargs.items():
            self.unpack.append([key] * val)

        # Convert list of lists into one list of hat contents
        for item in self.unpack:
            for word in item:
                self.contents.append(word)
        # print(self.contents)
        # print(kwargs)

    def draw(self, amount):
        pass



hat = Hat(one=1, two=2, yellow=7, green=5, test=10, whiteboy=2, password=5, omegalul=3, white=2)

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass