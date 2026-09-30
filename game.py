#import the pygame library 
import pygame 
import random
import time
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,0)
bullets=[]
bullet_rects=[]
enemy_list=[]
enemy_rects=[]
enemy_health=[]
#start the pygame module 
pygame.mixer.init()
pygame.init() 
#variables for screen size: 
screen_width=700
screen_height=1000
hasSpawned=False
threshold=85
#color code constants 
THE_END = (33, 24, 36)
RED=(200,0,0)
GRN=(0,200,0)
BLU=(0,0,200)
#other variable initializers (fonts, text, images, etc)
bullet='bullet_up.png'
mine='cosmic_mine.png'
player='player.png'
enemy='enemy.png'
bg_islands='BG.png'
boss='boss.png'
screen_go='GameOver.png'
x=325
scroll_y=-1024
firedMine=False
mine_cooldown=500
playerbase=850
frame_ticks=0
canFireMine=False
mx=x
bossSprite=pygame.image.load(boss)
bossRect=bossSprite.get_rect()
boss_y=-200
spawnedBoss=False
boss_health_base=1000
boss_health=boss_health_base
enemies_killed=0
enemies_escaped=0
state="Loop"
played=False
enemySpawnChance=0
my=playerbase
score=0
highscore=score
def draw_player(sprite, posx, posy):
  screen.blit(sprite, (posx, posy))
def update_bullet(rate):
  global score
  global enemies_killed
  global spawnedBoss
  global boss_health
  for i in range(0,len(bullets)-1):
    try:
      bullet_rects[i].y-=rate
      if bullet_rects[i].y <= -50:
        bullets.remove(bullets[i])
        bullet_rects.remove(bullet_rects[i])
      elif bullet_rects[i].colliderect(bossRect) and spawnedBoss==True:
        if boss_health<=0:
          spawnedBoss=False
          score+=2000
          kill.play()
          boom.play()
          bullets.remove(bullets[i])
          bullet_rects.remove(bullet_rects[i])
        else:
          boss_health-=5
          impact.play()
          bullets.remove(bullets[i])
          bullet_rects.remove(bullet_rects[i])
      for h in range(0, len(enemy_list)-1):
          if bullet_rects[i].colliderect(enemy_rects[h]):
            if enemy_health[h] <= 0:
              enemy_list.remove(enemy_list[h])
              enemy_rects.remove(enemy_rects[h])
              enemy_health.remove(enemy_health[h])
              score+=100
              kill.play()
              enemies_killed+=1
            else:
              enemy_health[h]-=25
              bullets.remove(bullets[i])
              bullet_rects.remove(bullet_rects[i])
              bulletenemysounds.play(impact)
    except IndexError:
      print("Bullet update failure!")
played2=False
def create_bullet():
  global playerbulletRect
  playerbulletSprite = pygame.image.load(bullet)
  bullets.append(playerbulletSprite)
  playerbulletRect = playerbulletSprite.get_rect()
  playerbulletRect.x=x
  playerbulletRect.y=850
  bullet_rects.append(playerbulletRect)  
def update_enemy(rate):
  global enemies_escaped
  try:
    for h in range(0,len(enemy_list)-1):
      enemy_rects[h].y+=rate
      if enemy_rects[h].y >= 1064:
        enemy_list.remove(enemy_list[h])
        enemy_rects.remove(enemy_rects[h])
        enemy_health.remove(enemy_health[h])
        enemies_escaped+=1
        alarm.play()
  except IndexError:
    print("Enemy update failure!")
def spawn_enemy(posx,posy,hp):
  global enemyRect
  enemySprite=pygame.image.load(enemy)
  enemy_list.append(enemySprite)
  enemyRect=enemySprite.get_rect()
  enemyRect.y=posy
  enemyRect.x=posx
  enemy_rects.append(enemyRect)
  enemy_health.append(hp)
def move_player(dir, modifier):
  global x
  if dir == 0:
    x-=modifier
  elif dir == 1:
    x+=modifier
cosmic_mine_sound = pygame.mixer.Sound("cosmic_mine_fire.mp3")
boom = pygame.mixer.Sound("boom.ogg")
cosmic_mine_recharge= pygame.mixer.Sound("cosmic_mine_recharge.mp3")
kill=pygame.mixer.Sound("enemy_dead.mp3")
impact=pygame.mixer.Sound("impact.mp3")
begin=pygame.mixer.Sound("start.mp3")
bulletenemysounds=pygame.mixer.Channel(1)
minesounds=pygame.mixer.Channel(2)
alarm=pygame.mixer.Sound("escape_warning.wav")
screenSprite=pygame.image.load(screen_go)
try:
  background = pygame.mixer.music.load("End.mp3")
  
  try:
    bulletenemysounds.play(begin,loops=0,maxtime=0,fade_ms=0)
    pygame.mixer.music.play(loops=-1, start=0.0, fade_ms=0) 
  except:
    print("Music file is not loaded, music cannot be played at this time.")
except:
  print("Missing the file for music, not playing music")
#create a screen with dimensions 
screen = pygame.display.set_mode((screen_width, screen_height))
font = pygame.font.SysFont("arial", 72)
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
  text = font.render(str(round(score)), True, GRN)
  texthigh = font.render(str(round(highscore)), True, GRN)
  text2=font.render(str(enemies_killed), True, GRN)
  text3=font.render(str(boss_health), True, BLU)
  text4=font.render(str(enemies_escaped), True, RED)
  playerbulletSprite = pygame.image.load(bullet)
  background=pygame.image.load(bg_islands)
  mineSprite = pygame.image.load(mine)
  playerSprite = pygame.image.load(player)
  pressed = pygame.key.get_pressed()
  if pressed[pygame.K_LEFT] and state=="Loop":
    move_player(0,7)
  elif pressed[pygame.K_RIGHT] and state=="Loop":
    move_player(1,7)
  score+=0.1
  print("Game is running")
  if pressed[pygame.K_m] and canFireMine == True and state=="Loop":
    if played2==False:
      played2=True
      minesounds.play(cosmic_mine_sound)
    canFireMine=False
    firedMine=True
    played=False
  if canFireMine==False and firedMine==True and state=="Loop":
    mx=mx
    my-=10
  else:
    mx=x
    my=playerbase
  if pressed[pygame.K_f] and state=="Loop":
    if frame_ticks == 15 or frame_ticks ==30 and state=="Loop":
      create_bullet()
  update_bullet(5)
  if my <= 200 and state=="Loop":
    try:
      for h in range(0,len(enemy_health)-1):
        enemy_health[h]-=10000
        enemy_list.remove(enemy_list[h])
        enemy_rects.remove(enemy_rects[h])
        enemy_health.remove(enemy_health[h])
        score+=100
        enemies_killed+=1
    except IndexError:
      print("Cosmic Mine failure!")
    minesounds.play(boom)
    played2=False
    mine_cooldown=1000
    my=playerbase
    firedMine=False
  if mine_cooldown <= 0 and state=="Loop":
    canFireMine=True
    if played==False and firedMine==False and state=="Loop":
      played=True
      minesounds.play(cosmic_mine_recharge)
    mine_cooldown=0
  else:
    mine_cooldown-=1
  if x >= 645 and state=="Loop":
    x=645
  if x <= -5 and state=="Loop":
    x=-5
  if len(enemy_list) <= 25 and frame_ticks == 15 and enemySpawnChance >=threshold and spawnedBoss==False and state=="Loop":
    spawn_enemy(random.randint(0,screen_width-64), -50, 200)
  #all items drawn to the screen go here
  screen.fill(THE_END)
  screen.blit(background, (-256, scroll_y))
  screen.blit(mineSprite, (mx, my))
  if enemies_killed >= 100 and spawnedBoss==False and hasSpawned==False and state=="Loop":
    spawnedBoss=True
    hasSpawned=True
  if spawnedBoss==True and state=="Loop":
    screen.blit(bossSprite, (234,boss_y))
    boss_y+=0.1
    bossRect.y=boss_y
    bossRect.x=234
    if boss_health == 1000 and state=="Loop":
      screen.blit(text3, (475, 825))
    elif boss_health <= 999 and boss_health >= 100 and state=="Loop":
      screen.blit(text3, (510, 825))
    elif boss_health <=99 and boss_health >=0 and state=="Loop":
      screen.blit(text3, (545, 825))
  if spawnedBoss==False and hasSpawned==True and state=="Loop":
    threshold=70
  for bullet_number in range(0,len(bullets)-1):
    screen.blit(bullets[bullet_number], (bullet_rects[bullet_number].x,bullet_rects[bullet_number].y))
  for enemy_c in range(0,len(enemy_list)-1):
    screen.blit(enemy_list[enemy_c], (enemy_rects[enemy_c].x,enemy_rects[enemy_c].y))
  draw_player(playerSprite, x, playerbase)
  if scroll_y >= 1024:
    scroll_y=-1024
  else:
    scroll_y+=2
  if enemies_escaped >=10:
    state="Game Over"
    score=0
    screen.blit(screenSprite, (100,200))
    if pressed[pygame.K_r]:
      state="Loop"
      enemies_escaped=0
      boss_y=-100
      boss_health=1000
      hasSpawned=False
      threshold=85
      spawnedBoss=False
      bullets.clear()
      bullet_rects.clear()
      enemy_list.clear()
      enemy_rects.clear()
      enemy_health.clear()
  elif score >= highscore:
    highscore=score
  screen.blit(text,(0, 900))
  screen.blit(texthigh,(0, 0))
  screen.blit(text2,(0, 825))
  screen.blit(text4, (600, 900))
  #This function call updates the screen 
  pygame.display.update() 
  update_enemy(1)
  print("\033[H\033[J", end="")
  #sets the frame rate
  clock.tick(60) 
  if frame_ticks >= 30:
    frame_ticks = 0
    enemySpawnChance=random.randint(0,100)
  else:
    frame_ticks+=1
#quits the pygame module 
pygame.quit() 
quit() 