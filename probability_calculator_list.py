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
            return draw_list
        else:
            for i in range(amount):
                random_ball = random.choice(draw_list)
                draw_list.remove(random_ball)
                draw_result.append(random_ball)
        
        return draw_result

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    experiment_draw = []
    count = 0
    experiment_success_count = 0
    
    for i in range(num_experiments):
        count = 0
        hat_copy = copy.deepcopy(hat)
        experiment_draw = hat_copy.draw(num_balls_drawn)
        
        for key, val in expected_balls.items():
            if experiment_draw.count(key) >= val:
                count += 1

        if count == len(expected_balls):
            experiment_success_count += 1

    probability = experiment_success_count / (num_experiments)
    return probability


# Testing
my_dict = {"yellow":1,"green":1}
their_dict = {"blue":2,"green":1}
hat = Hat(blue=3,red=2,green=6)
mine = Hat(yellow=2, green=2)
print('Contents theirs', hat.contents)
print('Contents mine', mine.contents)
print('My experiment', experiment(mine, my_dict, 5, 100))
print('Their experiment', experiment(hat, their_dict, 4, 1000))