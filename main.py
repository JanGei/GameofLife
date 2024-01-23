# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 18:06:02 2024

@author: Janek
"""

import pygame
import numpy as np
import sys
from functions import update, color_flurry, initial_state
import time

# Initialize Pygame
pygame.init()

# Set up the window
width, height = 1200, 800
window_size = (width, height)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Pygame Grid")

# Set up colors
white = (255, 255, 255)
black = (0, 0, 0)
# Set up grid parameters
grid_size = 10
grid_color = np.random.randint(0, 256, size = (3,256))

grid_size = 10
num_rows = height // grid_size
num_cols = width // grid_size

#initial state
state_matrix = initial_state(num_rows, num_cols, 'random')


# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw on the canvas
    screen.fill(white)
    
    # time.sleep(1)
    state_matrix = update(state_matrix, screen, grid_size)
    time.sleep(0.2)
    
    # Flurry of colors
    # color_flurry(state_matrix, screen, grid_size)

    # Update the display
    pygame.display.flip()


