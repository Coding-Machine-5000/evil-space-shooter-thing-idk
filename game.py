#import the pygame library 
import pygame 
import random
import time
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,0)
bullets=[]
bullet_rects=[]
enemy_list=[1,2,3,4,5]
enemy_rects=[]
enemy_health=[]
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
base=-50
safecheck=False
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
def update_bullet(rate):
  for i in range(0,len(bullets)-1):
    bullet_rects[i].y-=rate
    print(bullet_rects[i].y)
    if bullet_rects[i].y <= -50:
      bullets.remove(bullets[i])
      bullet_rects.remove(bullet_rects[i])
def create_bullet():
  global playerbulletRect
  playerbulletSprite = pygame.image.load(bullet)
  bullets.append(playerbulletSprite)
  playerbulletRect = playerbulletSprite.get_rect()
  playerbulletRect.x=x
  playerbulletRect.y=850
  bullet_rects.append(playerbulletRect)  
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
  playerbulletSprite = pygame.image.load(bullet)
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
  if pressed[pygame.K_f]:
    if frame_ticks == 10 or frame_ticks == 20 or frame_ticks == 30:
      create_bullet()
  update_bullet(5)
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
  for bullet_number in range(0,len(bullets)):
    screen.blit(bullets[bullet_number], (bullet_rects[bullet_number].x,bullet_rects[bullet_number].y))
  draw_player(playerSprite, x, playerbase)
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