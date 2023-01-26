import random
import time
import pygame
pygame.init()

class Button(pygame.sprite.Sprite):
    def __init__(self, color_on, color_off, sound, x, y):
        pygame.sprite.Sprite.__init__(self)
        # Vars
        self.color_on = color_on
        self.color_off = color_off
        self.sound = sound
        self.x = x
        self.y = y
        # Properties
        self.image = pygame.Surface((230, 230))
        self.image.fill(self.color_off)
        self.rect = self.image.get_rect()
        # Assign x, y coordinates to the top left of the sprite
        self.rect.topleft = (self.x, self.y)
        self.clicked = False

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def selected(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            return True
        else:
            return False

    def update(self, screen):
        # Fill color
        self.image.fill(self.color_on)
        # Blit
        screen.blit(self.image, (self.rect.x, self.rect.y))
        # Play sound
        pygame.mixer.Sound.play(self.sound)
        pygame.display.update()
        self.image.fill(self.color_off)
        screen.blit(self.image, (self.rect.x, self.rect.y))
        pygame.time.wait(500)
        pygame.display.update()
