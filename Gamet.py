#My first game project

import pygame 


#intializes pygame
pygame.init()


#Sets the dimensions of the gaming window to a tuple which is immutable 
gameDisplay = pygame.display.set_mode((800,600))

# Defining colors (R,G,B) 
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)


#Sets the game window title
pygame.display.set_caption('Slither Me Timbers')
gameExit = False

lead_x = 300
lead_y = 300


#Game Loop 
while not gameExit:
    #Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x -= 10
            if event.key == pygame.K_RIGHT:
                lead_x += 10

                            
    gameDisplay.fill(red)
    pygame.draw.rect(gameDisplay,black,[lead_x,lead_y,10,10])     #(where to draw it, color,[x,y,width,height])
    pygame.display.update()



#Unanitializes pygame display
pygame.quit()

#Quits python
quit()
