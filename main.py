import pygame
pygame.init()

###---setting up the window size using variables---###
x=0 #initialise x
y=0 #initialise y

width = 40 #sie of rect
height = 40 #size of rect

winx = 500
winy = 300
win = pygame.display.set_mode((winx,winy))
pygame.display.set_caption("Left, Right and Jump")


### basic graphics set up ###
bg = pygame.image.load('images/bg.jpg')
bg=pygame.transform.scale(bg,(winx, winy))

ship = pygame.image.load('images/ship.png')
ship=pygame.transform.scale(ship,(width, height))

###---positioning the rect in the middle


###--- position rect in middle and at the bottom---###
x = 250 #position of rect
y = 250  #position of rect


vel = 10 #velocity or attack value
jumpMax = 10 #set the number of iterations for the jump maths

### --- this is just to show you how abs (absolute value) works ###
### --- the absolute value of 20 is -20@
integer = -20
print('Absolute value of -20 is:', abs(integer))

isJump = False #start the routine in jump flag set to false
jumpCount = jumpMax # number of iterations for the jump loop.


####--- Begin Def Routines ---####

###-function for screen refresh

def redrawGameWindow():
  win.blit(bg, (0,0))  # This will draw our background image at (0,0)
  win.blit(ship,(x,y))
  pygame.display.update() 

run = True

while run:
    pygame.time.delay(60) #setting game run speed

    for event in pygame.event.get(): #listen for events
        if event.type == pygame.QUIT: #quit
            run = False

    keys = pygame.key.get_pressed() #set variable for which key is pressed
    
    if keys[pygame.K_LEFT] and x > vel:
      #if pressing left and positon of rect is greater than velocity - the movement speed in pixels
        x -= vel #move the rect left by velocity (5 in this case)

    if keys[pygame.K_RIGHT] and x < 500 - vel - width:  
        x += vel
        
    if not(isJump): 
        if keys[pygame.K_UP] and y > vel:
            y -= vel

        if keys[pygame.K_DOWN] and y < 500 - height - vel:
            y += vel

        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -jumpMax:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            print('jump grav', y) #show the maths
            jumpCount -= 1 #take away one from the loop
            print ('rect position',(jumpCount - y))
        else: 
            jumpCount = jumpMax
            isJump = False
    
    #win.fill((0,0,0))
    redrawGameWindow()
  
pygame.quit()