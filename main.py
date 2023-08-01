import pygame
import random

pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Snake properties
BLOCK_SIZE = 20
INITIAL_SPEED = 5

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')

# Helper function to display text on the screen


def display_text(text, font, color, x, y):
    surface = font.render(text, True, color)
    screen.blit(surface, (x, y))


# Main function for the game
def snake_game():
    clock = pygame.time.Clock()

    # Initialize the snake
    snake = [(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)]
    snake_length = 1

    # Add score
    score = 0

    # Initial direction of the snake (right)
    direction = (BLOCK_SIZE, 0)

    # Initialize the food
    food = generate_food(snake)

    # Game loop
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != (0, BLOCK_SIZE):
                    direction = (0, -BLOCK_SIZE)
                elif event.key == pygame.K_DOWN and direction != (0, -BLOCK_SIZE):
                    direction = (0, BLOCK_SIZE)
                elif event.key == pygame.K_LEFT and direction != (BLOCK_SIZE, 0):
                    direction = (-BLOCK_SIZE, 0)
                elif event.key == pygame.K_RIGHT and direction != (-BLOCK_SIZE, 0):
                    direction = (BLOCK_SIZE, 0)

        # Move the snake
        head_x, head_y = snake[-1]
        dx, dy = direction
        new_head = ((head_x + dx) % SCREEN_WIDTH,
                    (head_y + dy) % SCREEN_HEIGHT)

        if new_head in snake:
            # Snake collided with itself, game over
            game_over = True
        else:
            snake.append(new_head)
            if len(snake) > snake_length:
                del snake[0]

        # Check if the snake ate the food
        if snake[-1] == food:
            food = generate_food(snake)
            snake_length += 1
            score += 1

        # Draw everything on the screen
        screen.fill(BLACK)
        for segment in snake:
            pygame.draw.rect(
                screen, GREEN, (segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(
            screen, RED, (food[0], food[1], BLOCK_SIZE, BLOCK_SIZE))

        # Display score
        font = pygame.font.Font(None, 36)
        score_text = f"Score: {score}"
        score_surface = font.render(score_text, True, WHITE)
        screen.blit(score_surface, (10, 10))

        # Update the display
        pygame.display.update()

        # Control the speed of the game
        clock.tick(INITIAL_SPEED + snake_length)

    # Display game over message
    font = pygame.font.Font(None, 36)
    display_text("Game Over", font, WHITE, SCREEN_WIDTH //
                 2 - 80, SCREEN_HEIGHT // 2 - 20)
    pygame.display.update()

    # Wait for a moment before closing the game
    pygame.time.wait(2000)

# Helper function to generate random food position


def generate_food(snake):
    while True:
        x = random.randrange(0, SCREEN_WIDTH, BLOCK_SIZE)
        y = random.randrange(0, SCREEN_HEIGHT, BLOCK_SIZE)
        if (x, y) not in snake:
            return (x, y)


if __name__ == "__main__":
    snake_game()

pygame.quit()
