#import the pygame library 
import pygame 
import random
import time
#anchor the pygame screen so you see it in codio.
#Click on the arrow in the upper left corner to display in a new browser tab.
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,0)
bullets=[1,2,3]
enemy_list=[1,2,3,4,5]
#start the pygame module 
pygame.mixer.init()
pygame.init() 
#variables for screen size: 
screen_width=700
screen_height=1000
#color code constants 
THE_END = (33, 24, 36)
#other variable initializers (fonts, text, images, etc)
bullet='bullet_up.png'
mine='cosmic_mine.png'
player='player.png'
enemy='enemy.png'
bg_islands='BG.png'
x=325
scroll_y=-1024
firedMine=False
mine_cooldown=500
EnemyHealth1=50
EnemyHealth2=50
EnemyHealth3=50
EnemyHealth4=50
EnemyHealth5=50
playerbase=850
pb1y=playerbase
pb2y=playerbase
pb3y=playerbase
base=-50
#pb stands for Player Bullet
pb1x=x
pb2x=x
pb3x=x
e1y=base
e2y=base
e3y=base
e4y=base
e5y=base
bulletFireSelection=1
enemySelection=1
frame_ticks=0
current_bullet=0
canFire1=True
canFire2=True
canFire3=True
canFireMine=False
mx=x
my=playerbase
score=0
def draw_player(sprite, posx, posy):
  screen.blit(sprite, (posx, posy))
def update_bullet_1(rate):
  global pb1y
  pb1y-=rate
def update_bullet_2(rate):
  global pb2y
  pb2y-=rate
def update_bullet_3(rate):
  global pb3y
  pb3y-=rate
def update_enemy(e):
  global enemySelection
  enemySelection=e
def move_enemy():
  global enemySelection
  global e1y
  global e2y
  global e3y
  global e4y
  global e5y
  if enemySelection == 0:
    e1y+=1
    e2y+=0.5
    e3y+=0.5
    e4y+=0.5
    e5y+=0.5
  elif enemySelection == 1:
    e1y+=0.5
    e2y+=1
    e3y+=0.5
    e4y+=0.5
    e5y+=0.5
  elif enemySelection == 2:
    e1y+=0.5
    e2y+=0.5
    e3y+=1
    e4y+=0.5
    e5y+=0.5
  elif enemySelection == 3:
    e1y+=0.5
    e2y+=0.5
    e3y+=0.5
    e4y+=1
    e5y+=0.5
  elif enemySelection == 4:
    e1y+=0.5
    e2y+=0.5
    e3y+=0.5
    e4y+=0.5
    e5y+=1 
def move_player(dir, modifier):
  global x
  if dir == 0:
    x-=modifier
  elif dir == 1:
    x+=modifier
def fire_bullet(bul):
  global canFire1
  global canFire2
  global canFire3
  if bul == 1:
    canFire1=False
  if bul == 2:
    canFire2=False
  if bul == 3:
    canFire3=False
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
  playerbullet1Sprite = pygame.image.load(bullet)
  playerbullet2Sprite = pygame.image.load(bullet)
  playerbullet3Sprite = pygame.image.load(bullet)
  background=pygame.image.load(bg_islands)
  mineSprite = pygame.image.load(mine)
  enemySprite1 = pygame.image.load(enemy)
  enemySprite2 = pygame.image.load(enemy)
  enemySprite3 = pygame.image.load(enemy)
  enemySprite4 = pygame.image.load(enemy)
  enemySprite5 = pygame.image.load(enemy)
  playerSprite = pygame.image.load(player)
  pressed = pygame.key.get_pressed()
  if pressed[pygame.K_LEFT]:
    move_player(0,4)
  elif pressed[pygame.K_RIGHT]:
    move_player(1,4)
  score+=0.1
  print("\033[H\033[J", end="")
  print(mine_cooldown)
  print(round(score))
  if pressed[pygame.K_m] and canFireMine == True:
    canFireMine=False
    firedMine=True
  if canFireMine==False and firedMine==True:
    mx=mx
    my-=5
  else:
    mx=x
    my=playerbase  
  if my < 200:
    EnemyHealth1=0
    EnemyHealth2=0
    EnemyHealth3=0
    EnemyHealth4=0
    EnemyHealth5=0
    mine_cooldown=1000
    my=playerbase
    firedMine=False
  if mine_cooldown <= 0:
    canFireMine=True
    mine_cooldown=0
  else:  
    mine_cooldown-=1
  if x >= 645:
    x=645
  if x <= -5:
    x=-5
  if pb1y <= e1y + 20 and (pb1x <= 64 and pb1x >= -50):
      EnemyHealth1-=5
      canFire1=True
      pb1y=playerbase
  elif pb2y <= e1y + 20 and (pb2x <= 64 and pb2x >= -50):
      EnemyHealth1-=5
      canFire2=True
      pb2y=playerbase
  elif pb3y <= e1y + 20 and (pb3x <= 64 and pb3x >= -50):
      EnemyHealth1-=5
      canFire3=True
      pb3y=playerbase
  if pb1y <= e2y + 20 and (pb1x <= 214 and pb1x >= 100):
      EnemyHealth2-=5
      canFire1=True
      pb1y=playerbase
  elif pb2y <= e2y + 20 and (pb2x <= 214 and pb2x >= 100):
      EnemyHealth2-=5
      canFire2=True
      pb2y=playerbase
  elif pb3y <= e2y + 20 and (pb3x <= 214 and pb3x >= 100):
      EnemyHealth2-=5
      canFire3=True
      pb3y=playerbase
  if pb1y <= e3y + 20 and (pb1x <= 364 and pb1x >= 250):
      EnemyHealth3-=5
      canFire1=True
      pb1y=playerbase
  elif pb2y <= e3y + 20 and (pb2x <= 364 and pb2x >= 250):
      EnemyHealth3-=5
      canFire2=True
      pb2y=playerbase
  elif pb3y <= e3y + 20 and (pb3x <= 364 and pb3x >= 250):
      EnemyHealth3-=5
      canFire3=True
      pb3y=playerbase
  if pb1y <= e4y + 20 and (pb1x <= 514 and pb1x >= 400):
      EnemyHealth4-=5
      canFire1=True
      pb1y=playerbase
  elif pb2y <= e4y + 20 and (pb2x <= 514 and pb2x >= 400):
      EnemyHealth4-=5
      canFire2=True
      pb2y=playerbase
  elif pb3y <= e4y + 20 and (pb3x <= 514 and pb3x >= 400):
      EnemyHealth4-=5
      canFire3=True
      pb3y=playerbase
  if pb1y <= e5y + 20 and (pb1x <= 664 and pb1x >= 550):
      EnemyHealth5-=5
      canFire1=True
      pb1y=playerbase
  elif pb2y <= e5y + 20 and (pb2x <= 664 and pb2x >= 550):
      EnemyHealth5-=5
      canFire2=True
      pb2y=playerbase
  elif pb3y <= e5y + 20 and (pb3x <= 664 and pb3x >= 550):
      EnemyHealth5-=5
      canFire3=True
      pb3y=playerbase
  if EnemyHealth1 <= 0:
      EnemyHealth1=50
      score+=200
      e1y=base
  if EnemyHealth2 <= 0:
      score+=200
      EnemyHealth2=50
      e2y=base
  if EnemyHealth3 <= 0:
      EnemyHealth3=50
      score+=200
      e3y=base
  if EnemyHealth4 <= 0:
      EnemyHealth4=50
      score+=200
      e4y=base
  if EnemyHealth5 <= 0:
      EnemyHealth5=50
      score+=200
      e5y=base
  move_enemy()
  #all items drawn to the screen go here
  screen.fill(THE_END)
  screen.blit(background, (-256, scroll_y))
  screen.blit(mineSprite, (mx, my))
  screen.blit(enemySprite1, (0,e1y))
  screen.blit(enemySprite2, (150,e2y))
  screen.blit(enemySprite3, (300,e3y))
  screen.blit(enemySprite4, (450,e4y))
  screen.blit(enemySprite5, (600,e5y))
  screen.blit(playerbullet1Sprite, (pb1x, pb1y))
  screen.blit(playerbullet2Sprite, (pb2x, pb2y))
  screen.blit(playerbullet3Sprite, (pb3x, pb3y))
  draw_player(playerSprite, x, playerbase)
  if pressed[pygame.K_f]:
    if canFire1==True and current_bullet==0 and frame_ticks == 10:
      fire_bullet(1)
      current_bullet=1
    elif canFire2==True and current_bullet==1 and frame_ticks == 20:
      fire_bullet(2)
      current_bullet=2
    elif canFire3==True and current_bullet==2 and frame_ticks == 30:
      fire_bullet(3)
      current_bullet=0
  if pb1y != playerbase:
    pb1x = pb1x
  else:
    pb1x = x
  if canFire1==False:
    update_bullet_1(15)
    if pb1y <=-50:
      pb1y=playerbase
      canFire1=True
  if pb2y != playerbase:
    pb2x=pb2x
  else:
    pb2x = x
  if canFire2==False:
    update_bullet_2(15)
    if pb2y <=-50:
      pb2y=playerbase
      canFire2=True
  if pb3y != playerbase:
    pb3x=pb3x
  else:
    pb3x = x
  if canFire3==False:
    update_bullet_3(15)
    if pb3y <=-50:
      pb3y=playerbase
      canFire3=True
  if e1y > playerbase or e2y > playerbase or e3y > playerbase or e4y > playerbase or e5y > playerbase:
    print("Game Over! Restarting game!")
    time.sleep(5)
    x=345
    scroll_y=-1024
    e1y=-50
    e2y=-50
    e3y=-50
    e4y=-50
    e5y=-50
    score=0
  if scroll_y >= 1024:
    scroll_y=-1024
  else:
    scroll_y+=2
  #This function call updates the screen 
  pygame.display.update() 

  #sets the frame rate
  clock.tick(60) 
  if frame_ticks >= 30:
    frame_ticks = 0
    update_enemy(random.randint(0,4))
  else:
    frame_ticks+=1
#quits the pygame module 
pygame.quit() 
quit() 