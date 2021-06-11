import pygame
pygame.init()

winx = 500
winy = 300
win = pygame.display.set_mode((winx,winy))
pygame.display.set_caption("First Game")

x = 150 #position of rect
y = 290 #position of rect
width = 10 #sie of rect
height = 10 #size of rect
vel = 5 #velocity or attack value

isJump = False #start the routine in jump flag set to false
jumpCount = 10 # number of iterations for the jump loop.

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
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else: 
            jumpCount = 10
            isJump = False
    
    win.fill((0,0,0))
    pygame.draw.rect(win, (255,0,0), (x, y, width, height))   
    pygame.display.update() 
    
pygame.quit()