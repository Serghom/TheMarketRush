#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from pygame.sprite import Sprite
from pygame.image import load
from pygame import transform
from pygame import Rect


class World(Sprite):
    def __init__(self, filename, x, y, w, h, wa, ha):
        Sprite.__init__(self)
        self.image = load(filename).convert_alpha()
        self.image = transform.scale(self.image, (wa, ha))
        #self.rect = self.image.get_rect()
        self.rect = Rect(x, y, w, h)
        self.rect.x = x
        self.rect.y = y