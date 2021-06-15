import pygame
import sys
pygame.init()

clock = pygame.time.Clock()

###---setting up the window size using variables---###
x=0 #initialise x
y=0 #initialise y

width = 70 #sie of rect
height = 50 #size of rect

winx = 500
winy = 200
win = pygame.display.set_mode((winx,winy))
pygame.display.set_caption("Blitz")


### basic graphics set up ###
bg = pygame.image.load('images/bg.jpg')
bg=pygame.transform.scale(bg,(winx, winy))

plane = pygame.image.load('images/plane.png')
plane=pygame.transform.scale(plane,(width, height))

x = 0 #position of rect
y = 0  #position of rect

vel = 50 #velocity or attack value

isBomb = False #start the routine in bomb flag set to false

####--- Begin Def Routines ---####

def redrawGameWindow():
  win.blit(bg, (0,0))
  win.blit(plane,(x,y))
  pygame.display.update() 

run = True

while run:
  pygame.time.delay(60) #setting game run speed

  for event in pygame.event.get(): #listen for events
      if event.type == pygame.QUIT: #quit
          run = False

  keys = pygame.key.get_pressed() #set variable for which key is pressed

  ###---move plane right-X moves--###

  clock.tick(60)

  landed = False
  while landed is False:
    print('x',x,'y',y)

# move plane x to the left and then drop down until it reaches the bottom right.
      
  redrawGameWindow()

  

pygame.quit()