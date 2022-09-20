from turtle import width
import pygame, sys, math, json, gameassets as gmsts
from pygame.locals import QUIT

pygame.init()
pygame.mixer.init()
pygame.font.init()

#video graphics AAAAAAAAAAAAAAA

clock = pygame.time.Clock()
FPS = 60

#window
resolution = (800, 600)
screen = pygame.display.set_mode((resolution))
width = screen.get_width()
height = screen.get_height()
pygame.display.set_caption("The Rock, Scisor and Papers: Dynamite Show ")

#game variables
keys = pygame.key.get_pressed()
game_initialize = True
mainMenuDrawer = True
cutscene_1 = False
cutscene_1_2 = False
#font
font1 = pygame.font.SysFont('freesanbold.ttf', 25)

def DrawText (text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

#images
#title
TITLE = pygame.image.load("assets/sprites/title.png")

#button
play_button_image = pygame.image.load("assets/sprites/menu/buttons/play.png")

#cutscene things
cutscene_1_hawaii = pygame.image.load("assets/sprites/cutscene/hawaii.jpg").convert()
cutscene_frame = pygame.image.load("assets/sprites/cutscene/cutscene_frame.png")
text_box = pygame.image.load("assets/sprites/menu/hud/text_box.png")
the_rock_serious = pygame.image.load("assets/sprites/cutscene/rokiroki.jpeg").convert()
#backgrounds
main_menu_sky_paralax = pygame.image.load("assets/sprites/background/main_menu/sky_paralax.png").convert()
main_menu_clouds_paralax = pygame.image.load("assets/sprites/background/main_menu/sky_clouds.png").convert()
main_menu_mountains_paralax = pygame.image.load("assets/sprites/background/main_menu/mountains_paralax.png").convert()

#convert background
main_menu_sky_paralax = pygame.transform.scale(main_menu_sky_paralax, resolution)
main_menu_clouds_paralax = pygame.transform.scale(main_menu_clouds_paralax, resolution)
main_menu_mountains_paralax = pygame.transform.scale(main_menu_mountains_paralax, resolution)
#transform images
cutscene_frame = pygame.transform.scale(cutscene_frame, resolution)
cutscene_1_hawaii = pygame.transform.scale(cutscene_1_hawaii, resolution)
the_rock_serious = pygame.transform.scale(the_rock_serious, resolution)

#audio



#main menu
RSPDYSH = pygame.mixer.Sound('assets/audio/intro.mp3')
    #backgroud paralax function
def _paralax(img, vel):
    global width
    rel_width = width % img.get_rect().width
    screen.blit(img, (rel_width - img.get_rect().width, 0))
    if rel_width < 800:
        screen.blit(img, (rel_width, 0))
    width -= vel

#fadeFunction
def fade(invert):
  fade = pygame.Surface(resolution)
  if invert == False:
    fade.fill((0,0,0))
    for alpha in range(0, 255):
      fade.set_alpha(alpha)
      screen.blit(fade,(0,0))
      pygame.display.update()
      pygame.time.delay(10)
      invert = True
      
#phase emitter
# hackMenu
def hack_menu():
  mainMenuDrawer = False
  screen.fill((0, 0, 0))
  hack_menu_buttom = gmsts.Button(screen, 400, 400, play_button_image, 64, 64)
  if hack_menu_buttom.draw():
    mainMenuDrawer = True


# Fighter Class

class player():
  def __init__(self):
  def


#def cutscene_animation():
#  global play_button_image
#  play_button_image = pygame.transform.scale(play_button_image, (128, 128))
#  for angle in range(0, 360):
#    screen.blit(pygame.transform.rotate(play_button_image, angle), (400 -(play_button_image.get_width() / 2), 300 - (play_button_image.get_height() / 2)))
#   pygame.time.delay(10)
#    pygame.display.update()
#    if angle == 360:
#      angle = 0

while game_initialize:
  clock.tick(FPS)
  ev = pygame.event.wait()
  for event in pygame.event.get():
    if event.type == QUIT:
      game_initialize = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_a:
        print("Hello, i am your HackPrompt")
        hack_menu()

    #menu
    if mainMenuDrawer == True:
        _paralax(main_menu_sky_paralax, 0.1)
        screen.blit(TITLE, (175, 30))
        play_buttom = gmsts.Button(screen, 400, 400, play_button_image, 64, 64)
        if play_buttom.draw():
          fade(False)
          mainMenuDrawer = False
          cutscene_1 = True
        #paralax1 = gmsts.Animation(main_menu_sky_paralax, width, height, 0.1, screen)
        #paralax1._paralax()
  
    # Cutscene 1
    if cutscene_1 == True:
      _paralax(cutscene_1_hawaii, 1)
      screen.blit(cutscene_frame,(0, 0))
    if cutscene_1_2 == True:
      screen.fill((255,255,255))
      screen.blit(cutscene_frame,(0, 0))
    
    if battle == True:
      


  pygame.display.update()
pygame.quit()

