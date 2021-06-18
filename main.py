import pygame
import sys
pygame.init()
 
clock = pygame.time.Clock()
 
###---setting up the window size using variables---###
x=0 #initialise x
y=0 #initialise y
 
width = 70 #size of rect
height = 50 #size of rect
 
winx = 500
winy = 250
win = pygame.display.set_mode((winx,winy))
pygame.display.set_caption("Blitz")
 
### basic graphics set up ###
bg = pygame.image.load('images/bg.jpg')
bg=pygame.transform.scale(bg,(winx, winy))
 
plane = pygame.image.load('images/plane.png')
plane=pygame.transform.scale(plane,(width, height))

bomb = pygame.image.load('images/bomb.png')
bomb =pygame.transform.scale(bomb,(20, 20))
 
x = 0 #position of rect
y = 0  

bx=0
by=0 #bomb co-ordinates

speed=5 #plane speed
bspeed=10 #bomb speed
bombPress=False # bomb is invisible


###---Classes---##

 
####--- Begin Def Routines ---####
 
def redrawGameWindow():
  win.blit(bg, (0,0))
  win.blit(plane,(x,y))
  pygame.display.update() 
  
 
####--- Begin Main Loop ---####
 
run = True
bombPress = False
 
while run:
  pygame.time.delay(30) #setting game run speed
  by=y #track the plane
  bx=x
 
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit(); sys.exit()
        run = False
    
    # Condition becomes true when keyboard is pressed   
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        print("space pressed")

  
  ####--set up basic keys--###

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
          print('left')
      if event.key == pygame.K_RIGHT:
          print('right')
      if event.key == pygame.K_UP:
        print('jump')
      if event.key == pygame.K_DOWN:
        print(bombPress)

      
  
  #movement of plane
  x +=speed
  if x >= winx:
    y +=height
    x = 0
  
  #movement of bomb
  #if boomPress is True
 
  #Checking if the Plane has landed
  landed = False
  if x >= winx-width and y >= winy-height:
    landed = True
  
  if landed is True:
    print('The Plane has landed! ')
    while landed is True:
      x = winx-width
      y = winy-height
 
  redrawGameWindow()
 
pygame.quit()

