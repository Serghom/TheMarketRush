#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from pygame.sprite import Sprite
from pygame import Surface
from pygame import Rect
import pyganim
import animation
import time

class Drop(Sprite):

    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = Surface((60, 60))
        self.rect = Rect(0, 0, 60, 60)
        self.rect.x = x
        self.rect.y = y
        self.spawnTime = time.time()

        self.image.set_colorkey((0, 0, 40))

        self.animDrop = pyganim.PygAnimation(animation.LOOT)
        self.animDrop.play()

    def gravity(self):
        if time.time() - self.spawnTime > 0.5:
            self.rect.y += 4
        self.anim()

    def anim(self):
        self.image.fill((0, 0, 40))
        self.animDrop.blit(self.image, (0, 0))
