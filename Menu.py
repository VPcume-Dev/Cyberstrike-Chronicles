import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the window
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game Main Menu")

# Set up the colors
CYAN = (128, 255, 255)
BLUE = (0, 128, 255)
GREEN = (128, 255, 128)
BLACK = (0, 0, 0)
FONT = (255, 128, 128)
# Set up the fonts
title_font = pygame.font.Font(None, 64)
button_font = pygame.font.Font(None, 48)

# Set up the buttons
button_width, button_height = 200, 50
button_x = screen_width // 2 - button_width // 2
start_button_y = screen_height // 2 - 100
game_details_button_y = screen_height // 2
quit_button_y = screen_height // 2 + 100

# Set up the barrier
barrier_padding = 20
barrier_x = button_x - barrier_padding
barrier_y = start_button_y - barrier_padding - 10
barrier_width = button_width + 2 * barrier_padding
barrier_height = button_height * 3 + 4 * barrier_padding + 30
barrier_line_thickness = 5

# Render the title
title_text = "Cyberstrike Chronicles"
title_rendered = title_font.render(title_text, True, FONT)
title_rect = title_rendered.get_rect(center=(screen_width // 2, start_button_y - 100))

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_button_rect.collidepoint(pygame.mouse.get_pos()):
                print("Start Game button clicked")
                # Add your code to start the game here
            elif game_details_button_rect.collidepoint(pygame.mouse.get_pos()):
                print("Game Details button clicked")
                # Add your code to display game details here
            elif quit_button_rect.collidepoint(pygame.mouse.get_pos()):
                print("Quit button clicked")
                pygame.quit()
                sys.exit()

    # Clear the screen with a cyan background
    screen.fill(CYAN)

    # Draw the barrier background
    pygame.draw.rect(screen, GREEN, (barrier_x, barrier_y, barrier_width, barrier_height))

    # Draw the barrier line
    pygame.draw.rect(screen, BLUE, (barrier_x, barrier_y, barrier_width, barrier_line_thickness))
    pygame.draw.rect(screen, BLUE, (barrier_x, barrier_y, barrier_line_thickness, barrier_height))
    pygame.draw.rect(screen, BLUE, (barrier_x + barrier_width - barrier_line_thickness, barrier_y, barrier_line_thickness, barrier_height))
    pygame.draw.rect(screen, BLUE, (barrier_x, barrier_y + barrier_height - barrier_line_thickness, barrier_width, barrier_line_thickness))

    # Draw the title on the screen
    screen.blit(title_rendered, title_rect)

    # Render the buttons
    start_button = button_font.render("Start Game", True, BLACK)
    start_button_rect = start_button.get_rect(center=(screen_width // 2, start_button_y))
    game_details_button = button_font.render("Game Details", True, BLACK)
    game_details_button_rect = game_details_button.get_rect(center=(screen_width // 2, game_details_button_y))
    quit_button = button_font.render("Quit", True, BLACK)
    quit_button_rect = quit_button.get_rect(center=(screen_width // 2, quit_button_y))

    # Draw the buttons on the screen
    pygame.draw.rect(screen, GREEN, start_button_rect)
    pygame.draw.rect(screen, GREEN, game_details_button_rect)
    pygame.draw.rect(screen, GREEN, quit_button_rect)
    screen.blit(start_button, start_button_rect)
    screen.blit(game_details_button, game_details_button_rect)
    screen.blit(quit_button, quit_button_rect)

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()