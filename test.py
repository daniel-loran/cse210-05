import pygame
from pygame.locals import (K_i, K_k, K_j, K_l, K_ESCAPE, K_w, K_a, K_d, K_s, KEYDOWN, QUIT,)

p1_movement = 0
p2_movement = 0

pygame.init()   

BLACK = (0, 0, 0)
green = (0,255,0)

WIDTHTWO = 1
HEIGHTTWO = 1000
WIDTHONE = 2000
HEIGHTONE = 1000

pygame.display.set_caption("Tron")
screen = pygame.display.set_mode((1000,1000))
clock = pygame.time.Clock()
clock.tick(60)
screen.fill((0,0,0))

class PlayerOne(pygame.sprite.Sprite):
   p1_movement = 0
   def __init__(self):
       super(PlayerOne, self).__init__()
       self.surf = pygame.Surface((15, 10))
       self.surf.fill((255, 0, 0))
       self.rect = self.surf.get_rect()
       self.rect.center = (WIDTHONE / 2, HEIGHTONE / 2)
       self.trail = []

   def update(self, pressed_keys):
       if pressed_keys[K_i]:
           self.rect.move_ip(0, -1)
       if pressed_keys[K_k]:
           self.rect.move_ip(0, 1)
       if pressed_keys[K_j]:
           self.rect.move_ip(-1, 0)
       if pressed_keys[K_l]:
           self.rect.move_ip(1, 0)
       pos = self.rect.center
       if self.trail:
           if self.trail[-1] != pos:
               self.trail.append(pos)
       else:
           self.trail = [pos, pos]
       if self.rect.left < 0:
          self.rect.left = 0
       if self.rect.right > 1000:
          self.rect.right = 1000
       if self.rect.top <= 0:
          self.rect.top = 0
       if self.rect.bottom >= 1000:
          self.rect.bottom = 1000  
          
          

class PlayerTwo(pygame.sprite.Sprite):
   p1_movement = 0
   def __init__(self):
       super(PlayerTwo, self).__init__()
       self.surf = pygame.Surface((15, 10))
       self.surf.fill((0, 255, 255))
       self.rect = self.surf.get_rect()
       self.rect.center = (WIDTHTWO / 2, HEIGHTTWO / 2)
       self.trail = set()

   def update(self, pressed_keys):
       if pressed_keys[K_w]:
           self.rect.move_ip(0, -1)
       if pressed_keys[K_s]:
           self.rect.move_ip(0, 1)
       if pressed_keys[K_a]:
           self.rect.move_ip(-1, 0)
       if pressed_keys[K_d]:
           self.rect.move_ip(1, 0)
       pos = self.rect.center
       if self.trail:
           if self.trail[-1] != pos:
               self.trail.append(pos)
       else:
           self.trail = [pos, pos]
       if self.rect.left < 0:
          self.rect.left = 0
       if self.rect.right > 1000:
          self.rect.right = 1000
       if self.rect.top <= 0:
          self.rect.top = 0
       if self.rect.bottom >= 1000:
          self.rect.bottom = 1000    
    
    
player = PlayerOne()
playertwo = PlayerTwo()
running = True

while running:
   for event in pygame.event.get():
       if event.type == KEYDOWN:
           if event.key == K_ESCAPE:
               running = False       
       elif event.type == QUIT:
           running = False

   pressed_keys = pygame.key.get_pressed()
   
   player.update(pressed_keys)
   playertwo.update(pressed_keys)
   screen.fill((0, 0, 0))
   pygame.draw.lines(screen, (255, 255, 255), False, player.trail)
   pygame.draw.lines(screen, (255, 255, 255), False, playertwo.trail)
   screen.blit(player.surf, player.rect)
   screen.blit(playertwo.surf, playertwo.rect)
   pygame.display.flip()

pygame.quit()