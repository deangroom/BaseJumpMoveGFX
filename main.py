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
bombPress=False
 
####--- Begin Def Routines ---####
 
def redrawGameWindow():
  win.blit(bg, (0,0))
  win.blit(plane,(x,y))
  win.blit(bomb,(bx,by))
  pygame.display.update() 
  
 
####--- Begin Main Loop ---####
 
run = True
bombPress = False
 
while run:
  pygame.time.delay(30) #setting game run speed
 
  for event in pygame.event.get(): #listen for events
    if event.type == pygame.QUIT: #quit
      run = False
    if event.type == pygame.K_SPACE:
      print('bombs away')
      bombPress=True
      by=y
      
  
  #movement of plane
  x +=speed
  if x >= winx:
    y +=height
    x = 0
 
  #Checking if the Plane has landed
  landed = False
  print(landed)
  if x >= winx-width and y >= winy-height:
    landed = True
  
  if landed is True:
    print('The Plane has landed! ')
    while landed is True:
      x = winx-width
      y = winy-height
 
  redrawGameWindow()
 
pygame.quit()

