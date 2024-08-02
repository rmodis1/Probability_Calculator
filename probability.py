import copy
import random

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for color, count in balls.items():
            self.contents.extend([color] * count)

# If the number of balls to draw is greater than the number of balls in the hat,
# return all the balls and clear the contents of the hat.
    def draw(self, num_balls):
        if num_balls > len(self.contents):
            drawn_balls = self.contents.copy()
            self.contents.clear()
            return drawn_balls
        # Otherwise, randomly sample the specified number of balls from the hat.
        drawn_balls = random.sample(self.contents, num_balls)
        # Remove each drawn ball from the contents of the hat.
        for ball in drawn_balls:
            self.contents.remove(ball)
        # Return the list of drawn balls.
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0

    # Perform the experiment the specified number of times.
    for _ in range(num_experiments):
        # Create a deep copy of the hat to ensure the original hat is not modified.
        hat_copy = copy.deepcopy(hat)
        
        # Draw the specified number of balls from the hat copy.
        drawn_balls = hat_copy.draw(num_balls_drawn)
        
        # Count the number of each color of ball drawn.
        drawn_balls_count = {color: drawn_balls.count(color) for color in set(drawn_balls)}
        
        # Check if the drawn balls meet the expected criteria.
        success = True
        for color, count in expected_balls.items():
            if drawn_balls_count.get(color, 0) < count:
                success = False
                break
        
        # If the criteria are met, increment the success count.
        if success:
            success_count += 1

    # Return the probability of success.
    return success_count / num_experiments

#Example for testing
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=2000)
print(f"Probability: {probability}")