import pygame
import os
import random

WIDTH, HEIGHT = 900, 500
CHARACTER_WIDTH, CHARACTER_HEIGHT = 120, 120
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lamp Warrior")


WHITE = (255, 255, 255)

FPS = 60
VEL = 10

PLAYER_TOKEN_IMAGE = pygame.image.load(os.path.join('Assets', 'jake_drawing.png'))
PLAYER_TOKEN = pygame.transform.scale(PLAYER_TOKEN_IMAGE, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
print("Initializing fonts")
fonts = pygame.font.get_fonts()
print(len(fonts))
for f in fonts:
    print(f)

def draw_window(lamp):
    WIN.fill(WHITE)
    WIN.blit(PLAYER_TOKEN, (lamp.x, lamp.y))
    pygame.display.update()

# Function to handle the character's movement.
def lamp_handle_movement(keys_pressed, lamp):
        if keys_pressed[pygame.K_LEFT] and lamp.x > 0: # LEFT
            lamp.x -= VEL
        if keys_pressed[pygame.K_RIGHT] and lamp.x + lamp.width < WIDTH: # RIGHT
            lamp.x += VEL
        if keys_pressed[pygame.K_UP] and lamp.y - VEL > 0: # UP
            lamp.y -= VEL
        if keys_pressed[pygame.K_DOWN] and lamp.y + VEL + lamp.height < HEIGHT: # DOWN
            lamp.y += VEL

def main():
    lamp = pygame.Rect(100, 300, CHARACTER_WIDTH, CHARACTER_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        keys_pressed = pygame.key.get_pressed()
        lamp_handle_movement(keys_pressed, lamp)
        draw_window(lamp)

        
    pygame.quit()

if __name__ == "__main__":
    main()