import pygame
import random

# Initialize Pygame
pygame.init()

# Define the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set the screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set the block dimensions
BLOCK_SIZE = 10

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Define the font
font = pygame.font.SysFont(None, 25)

# Define the function to display the message
def message(msg, color):
    text = font.render(msg, True, color)
    screen.blit(text, [SCREEN_WIDTH/6, SCREEN_HEIGHT/3])

# Define the function to create the snake
def snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, GREEN, [x[0], x[1], block_size, block_size])

# Define the main function
def gameLoop():
    gameExit = False
    gameOver = False

    # Set the initial position of the snake
    lead_x = SCREEN_WIDTH / 2
    lead_y = SCREEN_HEIGHT / 2

    # Set the initial movement of the snake
    lead_x_change = 0
    lead_y_change = 0

    # Create the snake list and length
    snake_list = []
    snake_length = 1

    # Set the initial position of the food
    food_x = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / 10.0) * 10.0
    food_y = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / 10.0) * 10.0

    # Start the game loop
    while not gameExit:

        # If the game is over
        while gameOver == True:
            screen.fill(WHITE)
            message("Game over! Press Q to quit or C to play again", RED)
            pygame.display.update()

            # Check for user input
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # Check for user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -BLOCK_SIZE
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = BLOCK_SIZE
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -BLOCK_SIZE
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = BLOCK_SIZE
                    lead_x_change = 0

        # Move the snake
        lead_x += lead_x_change
        lead_y += lead_y_change

        # Check for collision with the boundaries
        if lead_x >= SCREEN_WIDTH or lead_x < 0 or lead_y >= SCREEN_HEIGHT or lead_y < 0:
            gameOver = True

        # Create the snake head
        snake_head = []
        snake_head.append(lead_x)
        snake_head.append(lead_y)
        snake_list.append(snake_head)

        # If the snake has grown
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check for collision with the food
        if lead_x == food_x and lead_y == food_y:
            food_x = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / 10.0) * 10.0
            food_y = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / 10.0) * 10.0
            snake_length += 1

        # Fill the screen with white color
        screen.fill(WHITE)

        # Draw the food
        pygame.draw.rect(screen, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])

        # Draw the snake
        snake(BLOCK_SIZE, snake_list)

        # Update the display
        pygame.display.update()

        # Set the frame rate
        clock = pygame.time.Clock()
        clock.tick(15)

    # Quit Pygame
    pygame.quit()

# Call the main function
gameLoop()
