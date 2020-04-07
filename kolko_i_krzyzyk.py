import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 50
HEIGHT = 50
 
# This sets the margin between each cell
MARGIN = 2
 
grid = []
for row in range(8):
    grid.append([])
    for column in range(8):
        grid[row].append(0)  # Append a cell
 
#punkt początkowy
grid[0][0] = 1
#pozycja na osi x
x = 0 
#pozycja na osi Y
y = 0
#aktualna pozycja

# Initialize pygame
pygame.init()
 
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [420, 420]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
#Tytuł okna
pygame.display.set_caption("Krata traktora")
 
# Loop until the user clicks the close button.
done = False
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        ''' elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            # Set that location to one
            grid[row][column] = 1
            print("Click ", pos, "Grid coordinates: ", row, column)
        '''
        pressed = pygame.key.get_pressed()
        # Change the x/y screen coordinates to grid coordinates
        column = pressed[0] // (WIDTH + MARGIN)
        row = pressed[1] // (HEIGHT + MARGIN)        
        #przejscie w prawo
        if pressed[pygame.K_RIGHT]:
            #sprawdzenie czy jest na krawędzi
            if column == 7:
                grid[row][column] = 1
                x = column
                y = row
            else:
                grid[row][column+1] = 1
                x = column +1
                y = row
                grid[row][column] == 2
                
        #przejscie w lewo
        if pressed[pygame.K_LEFT]:
            #sprawdzenie czy jest na krawędzi
            if column == 0:
                grid[row][column] = 1
            else:
                grid[row][column-1] = 1
        #przejscie w górę
        if pressed[pygame.K_UP]:
            #sprawdzenie czy jest na krawędzi
            if row == 0:
                grid[row][column] = 1
            else:
                grid[row-1][column] = 1
        #przejscie w dół
        if pressed[pygame.K_DOWN]:
            #sprawdzenie czy jest na krawędzi
            if row == 7:
                grid[row][column] = 1
            else:
                grid[row+1][column] = 1  

 
    #tło
    screen.fill(BLACK)
 
    # Draw the grid
    for row in range(8):
        for column in range(8):
            color = WHITE
            if grid[row][column] == 1:
                color = RED
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
            
 


    # Limit to 60 frames per second
    #clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
# on exit.
pygame.quit()