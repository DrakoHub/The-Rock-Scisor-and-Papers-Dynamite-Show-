import pygame

#button class
class Button():

    def __init__(self, surface, x, y, image, size_x, size_y):
        self.image = pygame.transform.scale(image, (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.surface = surface

    def draw(self):
        action = False

        #get mouse position
        pos = pygame.mouse.get_pos()

        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #draw button
        self.surface.blit(self.image, (self.rect.x, self.rect.y))

        return action

class Animation():

  def __init__(self, image, size_x, size_y, velocity, surface,):
    self.image = pygame.transform.scale(image, (size_x, size_y))
    self.velocity = velocity
    self.surface = surface
    self.size_x = size_x
    self.size_y = size_y
    self.rel_width = size_x % image.get_rect().width
  def _paralax(self):
    rel_width = self.size_x % self.image.get_rect().width
    self.surface.blit(self.image, (rel_width - self.image.get_rect().width, 0))
    if rel_width < self.size_x:
      self.surface.blit(self.image, (rel_width, 0))
    self.size_x -= self.velocity

