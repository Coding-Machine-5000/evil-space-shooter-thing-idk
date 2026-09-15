#import the pygame library 
import pygame 
import random
#anchor the pygame screen so you see it in codio.
#Click on the arrow in the upper left corner to display in a new browser tab.
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,0)
bullets=[1,2,3]

#start the pygame module 
pygame.mixer.init()
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
playerbullet1='bullet_up.png'
playerbullet2='bullet_up.png'
playerbullet3='bullet_up.png'
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
pb1y=playerbase
pb2y=playerbase
pb3y=playerbase
base=-50
pb1x=x
pb2x=x
pb3x=x
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
canFire1=True
canFire2=True
canFire3=True
try:
  background = pygame.mixer.music.load("End.mp3")
  try:
    pygame.mixer.music.play(loops=-1, start=0.0, fade_ms=0) 
  except:
    print("Music file is not loaded, music cannot be played at this time.")
except:
  print("Missing the file for music, not playing music")

#create a screen with dimensions 
screen = pygame.display.set_mode((screen_width, screen_height)) 

#set the screen caption 
pygame.display.set_caption("The End: The Space Shooter") 
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
  playerbullet1Sprite = pygame.image.load(playerbullet1)
  playerbullet2Sprite = pygame.image.load(playerbullet2)
  playerbullet3Sprite = pygame.image.load(playerbullet3)
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
    x-=7
  elif pressed[pygame.K_RIGHT]:
    x+=7

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
  screen.blit(playerbullet1Sprite, (pb1x, pb1y))
  screen.blit(playerbullet2Sprite, (pb2x, pb2y))
  screen.blit(playerbullet3Sprite, (pb3x, pb3y))
  screen.blit(playerSprite, (x, playerbase))
  if pressed[pygame.K_f]:
    if canFire1==True and current_bullet==0 and frame_ticks == 10:
      canFire1=False
      current_bullet=1
      print("Bullet ",bullets[current_bullet]," selected")
    elif canFire2==True and current_bullet==1 and frame_ticks == 20:
      canFire2=False
      current_bullet=2
      print("Bullet ",bullets[current_bullet]," selected")
    elif canFire3==True and current_bullet==2 and frame_ticks == 30:
      canFire3=False
      current_bullet=0
      print("Bullet ",bullets[current_bullet]," selected")
  if pb1y != playerbase:
    pb1x = pb1x + random.randint(-2,2)
  else:
    pb1x = x
  if canFire1==False:
    pb1y-=15
    if pb1y <=-50:
      pb1y=playerbase
      canFire1=True
  if pb2y != playerbase:
    pb2x=pb2x + random.randint(-2,2)
  else:
    pb2x = x
  if canFire2==False:
    pb2y-=15
    if pb2y <=-50:
      pb2y=playerbase
      canFire2=True
  if pb3y != playerbase:
    pb3x=pb3x + random.randint(-2,2)
  else:
    pb3x = x
  if canFire3==False:
    pb3y-=15
    if pb3y <=-50:
      pb3y=playerbase
      canFire3=True

  #This function call updates the screen 
  pygame.display.update() 

  #sets the frame rate
  clock.tick(60) 
  if frame_ticks >= 30:
    frame_ticks = 0
    enemySelection=random.randint(1,5)
  else:
    frame_ticks+=1
#quits the pygame module 
pygame.quit() 
quit() 