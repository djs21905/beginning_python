#My first game project
import pygame , time


#intializes pygame
pygame.init()


#Sets the dimensions of the gaming window to a tuple which is immutable
displayWidth = 800
displayHeight = 600
gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))

# Defining colors (R,G,B) 
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

font = pygame.font.SysFont(None,25)

#Functions
def message_to_screen(msg,color):
    screen_text = font.render(msg,True,color)
    gameDisplay.blit(screen_text,[displayWidth/2 , displayHeight/2])

#Sets the game window title
pygame.display.set_caption('Slither Me Timbers')
gameExit = False

clock = pygame.time.Clock()
fps = 60
block_size = 10 

lead_x = displayWidth/2
lead_y = displayHeight/2
lead_x_change = 0
lead_y_change = 0

#Game Loop 
while not gameExit:
    #Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -2
                lead_y_change = 0
            elif event.key == pygame.K_RIGHT:
                lead_x_change = 2
                lead_y_change = 0
            elif event.key == pygame.K_UP:
                lead_y_change = -2
                lead_x_change = 0
            elif event.key == pygame.K_DOWN:
                lead_y_change = 2
                lead_x_change = 0        
        if lead_x >= displayWidth or lead_x <= 0 or lead_y >= displayHeight or lead_y <= 0:
            gameExit = True
        
        
    lead_x += lead_x_change   # lead_x = lead_x + lead_x_change   
    lead_y += lead_y_change
                            
    gameDisplay.fill(red)
    pygame.draw.rect(gameDisplay,black,[lead_x,lead_y,block_size,block_size])     #(where to draw it, color,[x,y,width,height])
    pygame.display.update()

    clock.tick(fps)


message_to_screen('You lost the game! Good job noob..',white)
pygame.display.update()
time.sleep(2)
#Unanitializes pygame display
pygame.quit()

#Quits python
quit()
