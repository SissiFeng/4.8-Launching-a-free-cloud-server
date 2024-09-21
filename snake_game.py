import random
import time
import os

class SnakeGame:
    def __init__(self, width=20, height=20):
        self.width = width
        self.height = height
        self.snake = [(width // 2, height // 2)]
        self.direction = random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])
        self.food = self.generate_food()
        self.score = 0

    def generate_food(self):
        while True:
            food = (random.randint(0, self.width - 1), random.randint(0, self.height - 1))
            if food not in self.snake:
                return food

    def move_snake(self):
        # TODO: Implement snake movement
        # 1. Get the current head position
        # 2. Calculate the new head position based on self.direction
        # 3. Add the new head to the beginning of self.snake
        # 4. If the snake didn't eat food, remove the last segment
        # 5. Check if the snake has collided with the wall or itself
        pass

    def change_direction(self, new_direction):
        # TODO: Implement direction change
        # Make sure the new direction is valid (e.g., can't go directly opposite)
        pass

    def is_collision(self):
        # TODO: Implement collision detection
        # Check if the snake has hit the wall or itself
        pass

    def update(self):
        # TODO: Implement game state update
        # 1. Move the snake
        # 2. Check for collision
        # 3. Check if food is eaten, update score and generate new food if needed
        pass

    def draw(self):
        # TODO: Implement game rendering
        # Create a 2D list representing the game board
        # Draw the snake, food, and borders
        # Return the game board as a string
        pass

def main():
    game = SnakeGame()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(game.draw())
        print(f"Score: {game.score}")
        
        # TODO: Implement user input handling
        # Get user input and change game.direction accordingly
        
        game.update()
        time.sleep(0.1)
        
        if game.is_collision():
            print("Game Over!")
            break

if __name__ == "__main__":
    main()
