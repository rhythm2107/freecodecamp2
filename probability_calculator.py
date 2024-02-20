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

    def draw(self, amount):
        draw_list = self.contents
        draw_result = []

        if amount > len(draw_list):
            raise ValueError("The amount of draws exceeds the amount of balls in the hat.")

        print('This is the full list before draw\n', draw_list)
        for i in range(amount):
            random_ball = random.choice(draw_list)
            draw_list.remove(random_ball)
            draw_result.append(random_ball)
        print('This is the remaining list\n', draw_list)
        print('This is the list of results\n', draw_result)



hat = Hat(one=1, two=2, yellow=7, green=5, test=10, whiteboy=2, password=5, omegalul=3, white=2)
hat.draw(15)

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass