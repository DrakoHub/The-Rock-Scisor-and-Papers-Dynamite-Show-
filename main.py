from turtle import width
import pygame, sys, math, gameassets as gmsts
from pygame.locals import QUIT

pygame.init()
pygame.mixer.init()
pygame.font.init()
#video graphics AAAAAAAAAAAAAAA
clock = pygame.time.Clock()
FPS = 60
#window
resolution = (800, 600)
screen = pygame.display.set_mode(resolution)
width = screen.get_width()
height = screen.get_height()
pygame.display.set_caption("The Rock, Scisor and Papers: Dynamite Show ")
#game variables
game_initialize = True
mainMenuDrawer = True
cutscene1 = False
#font
font1 = pygame.font.SysFont('freesanbold.ttf', 50)
#images
#title
TITLE = pygame.image.load("assets/sprites/title.png")
#button
play_button_image = pygame.image.load("assets/sprites/menu/buttons/play.png")
#cutscene things
cutsene_maya_calender = pygame.image.load("assets/sprites/cutscene/calender.png")
cutscene_frame = pygame.image.load("assets/sprites/cutscene/cutscene_frame.png")
#backgrounds
main_menu_sky_paralax = pygame.image.load("assets/sprites/background/main_menu/sky_paralax.png").convert()
main_menu_clouds_paralax = pygame.image.load("assets/sprites/background/main_menu/sky_clouds.png").convert()
main_menu_mountains_paralax = pygame.image.load("assets/sprites/background/main_menu/mountains_paralax.png").convert()
#convert background
main_menu_sky_paralax = pygame.transform.scale(main_menu_sky_paralax, resolution)
main_menu_clouds_paralax = pygame.transform.scale(main_menu_clouds_paralax, resolution)
main_menu_mountains_paralax = pygame.transform.scale(main_menu_mountains_paralax, resolution)
#transform images
def _transform(image, size):
  image = pygame.transform.scale(image, size)
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
def fade_out(): 
  fade = pygame.Surface(resolution)
  fade.fill((0,0,0))
  for alpha in range(0, 255):
    fade.set_alpha(alpha)
    screen.blit(fade,(0,0))
    pygame.display.update()
    pygame.time.delay(5)
    #phase emitter
def main_menu():
  global mainMenuDrawer, cutscene1
  paralax1 = gmsts.Animation(main_menu_sky_paralax, width, height, 0.1, screen)
  paralax1._paralax()
  #_paralax(main_menu_sky_paralax, 0.1)
  screen.blit(TITLE, (175, 30))
  play_buttom = gmsts.Button(screen, 400, 400, play_button_image, 64, 64)
  if play_buttom.draw():
    fade_out()
    mainMenuDrawer = False
    cutscene1 = True
  if cutscene1 == True:
    cutscene1()
#def cutscene_animation():
#  global play_button_image
#  play_button_image = pygame.transform.scale(play_button_image, (128, 128))
#  for angle in range(0, 360):
#    screen.blit(pygame.transform.rotate(play_button_image, angle), (400 -(play_button_image.get_width() / 2), 300 - (play_button_image.get_height() / 2)))
#   pygame.time.delay(10)
#    pygame.display.update()
#    if angle == 360:
#      angle = 0

def cutscene1():
  global resolution, cutscene_frame
  text1 = font1.render('A', True, (0, 255, 0))
  screen.blit(text1, (250, 250))
  cutscene_frame = pygame.transform.scale(cutscene_frame, resolution)
  screen.blit(cutscene_frame, (0,0))

while game_initialize:
  clock.tick(FPS)
  if mainMenuDrawer == True:
    main_menu()
  for event in pygame.event.get():
      if event.type == QUIT:
        game_initialize = False
  pygame.display.update()
pygame.quit()

