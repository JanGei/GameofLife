import numpy as np
import pygame
import copy

def initial_state(num_rows, num_cols, cond = 'random'):
    
    if cond == 'random':
        state_matrix = np.random.rand(num_rows, num_cols)
        state_matrix = (state_matrix > 0.5).astype(int)
    elif cond == 'glider':
        pass
        
    return state_matrix

def update(oldstate, screen, grid_size):
    num_row,num_col = np.shape(oldstate)
    
    #define some rules later
    neighbour = count_neighbours(oldstate)
    
    newstate = copy.deepcopy(oldstate)
    newstate[np.logical_or(neighbour < 2, neighbour > 3)] = 0
    newstate[neighbour == 3] = 1
    # random updates
    # oldstate = np.random.rand(num_row,num_col)
    # oldstate = (oldstate > 0.5).astype(int)
    grid_color = np.random.randint(0, 256, size = (3,512))
    
    # newstate = 2
    
    
    for row in range(num_row):
        for col in range(num_col):
            if newstate[row,col]:
                # pygame.draw.rect(screen, (0,0,0), (col * grid_size, row * grid_size, grid_size, grid_size))
                pygame.draw.rect(screen, grid_color[:,np.random.randint(0, 256)], (col * grid_size, row * grid_size, grid_size, grid_size))
            else:
                pygame.draw.rect(screen, (255,255,255), (col * grid_size, row * grid_size, grid_size, grid_size))
    
    return newstate

def color_flurry(grid, screen, grid_size):
    grid_color = np.random.randint(0, 256, size = (3,512))
    
    num_row,num_col = np.shape(grid)
    for row in range(num_row):
        for col in range(num_col):
            pygame.draw.rect(screen, grid_color[:,np.random.randint(0, 256)], (col * grid_size, row * grid_size, grid_size, grid_size))
 
def count_neighbours(oldstate):
    nrow,ncol  = np.shape(oldstate)
    neighbour  = copy.deepcopy(oldstate)
    
    for row in range(nrow):
        for col in range(ncol):
            count = 0
            
            # Oberes Ende ist gesichert
            if row == 0:
                if col == 0:
                    count += (oldstate[row, col+1] + oldstate[row+1, col] +
                              oldstate[row+1, col+1])
                elif col == ncol-1:
                    count += (oldstate[row, col-1] + oldstate[row+1, col] +
                              oldstate[row-1, col-1])
                else:
                    count += (oldstate[row, col-1] + oldstate[row, col+1] +
                              oldstate[row+1, col-1] + oldstate[row+1, col] +
                              oldstate[row+1, col+1]) 
                    
            # Unteres Ende ist gesichert    
            elif row == nrow-1:
                if col == 0:
                    count += (oldstate[row, col+1] + oldstate[row-1, col] +
                              oldstate[row-1, col+1])
                elif col == ncol-1:
                    count += (oldstate[row, col-1] + oldstate[row-1, col] +
                              oldstate[row-1, col-1])
                else:
                    count += (oldstate[row, col-1] + oldstate[row, col+1] +
                              oldstate[row-1, col-1] + oldstate[row-1, col] +
                              oldstate[row-1, col+1]) 
            
            # Linker Rand ist gesichert
            elif col == 0:
                count += (oldstate[row+1, col] + oldstate[row+1, col+1] +
                          oldstate[row-1, col] + oldstate[row-1, col+1] +
                          oldstate[row, col+1]) 
                
            # Rechter Rand ist gesichert
            elif col == ncol -1:
                count += (oldstate[row+1, col] + oldstate[row+1, col-1] +
                          oldstate[row-1, col] + oldstate[row-1, col-1] +
                          oldstate[row, col-1]) 
            else:
                count += (oldstate[row-1, col-1] + oldstate[row-1, col] +
                          oldstate[row-1, col+1] + oldstate[row, col-1] +
                          oldstate[row, col+1]   + oldstate[row+1, col-1] +
                          oldstate[row+1, col] + oldstate[row+1, col+1]) 
            
            neighbour[row, col] = count
            
    return neighbour

            