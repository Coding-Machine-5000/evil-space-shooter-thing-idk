#import the pygame library 
import pygame 
import random
#anchor the pygame screen so you see it in codio.
#Click on the arrow in the upper left corner to display in a new browser tab.
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,0)
bullets=[]
bullet_positions=[]
#start the pygame module 
pygame.init() 

#variables for screen size: 
screen_width=700
screen_height=1000

#color code constants 
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
THE_END = (33, 24, 36)
#other variable initializers (fonts, text, images, etc)
playerbullet='bullet_up.png'
enemybullet='bullet_down.png'
mine='cosmic_mine.png'
player='player.png'
enemy1='enemy.png'
enemy2='enemy.png'
enemy3='enemy.png'
enemy4='enemy.png'
enemy5='enemy.png'
x=325
playerbase=850
pby=playerbase
base=-50
pbx=0
eby=base
e1y=base
e2y=base
e3y=base
e4y=base
e5y=base
bulletFireSelection=1
enemySelection=1
frame_ticks=0
e1in=False
e2in=False
e3in=False
e4in=False
e5in=False
current_bullet=0
#create a screen with dimensions 
screen = pygame.display.set_mode((screen_width, screen_height)) 

#set the screen caption 
pygame.display.set_caption("Random Space Shooter") 
screen.fill(THE_END)

 

#the clock will be used to regulate the frame rate 
clock = pygame.time.Clock() 

#variable to control the game loop 
keep_playing=True 

#Game Loop - needed to keep updating and redrawing the screen 
while keep_playing==True: 

  #iterates over the current list of events(checks for events)  
  for event in pygame.event.get(): 
    #will stop the game loop if escape is pressed 
    if event.type == pygame.QUIT:
      keep_playing = False
  playerbulletSprite = pygame.image.load(playerbullet)
  enemybulletSprite = pygame.image.load(enemybullet)
  mineSprite = pygame.image.load(mine)
  enemySprite1 = pygame.image.load(enemy1)
  enemySprite2 = pygame.image.load(enemy2)
  enemySprite3 = pygame.image.load(enemy3)
  enemySprite4 = pygame.image.load(enemy4)
  enemySprite5 = pygame.image.load(enemy5)
  playerSprite = pygame.image.load(player)
  pressed = pygame.key.get_pressed()
  if pressed[pygame.K_LEFT]:
    x-=3
  elif pressed[pygame.K_RIGHT]:
    x+=3

  if x >= 645:
    x=645
  if x <= -5:
    x=-5
  #all items drawn to the screen go here
  screen.fill(THE_END)

  screen.blit(enemySprite1, (0,e1y))
  screen.blit(enemySprite2, (150,e2y))
  screen.blit(enemySprite3, (300,e3y))
  screen.blit(enemySprite4, (450,e4y))
  screen.blit(enemySprite5, (600,e5y))
  screen.blit(playerSprite, (x, playerbase))
  #This function call updates the screen 
  pygame.display.update() 

  #sets the frame rate
  clock.tick(60) 
  if frame_ticks >= 60:
    frame_ticks = 0
    enemySelection=random.randint(1,5)
  else:
    frame_ticks+=1
#quits the pygame module 
pygame.quit() 
quit() 