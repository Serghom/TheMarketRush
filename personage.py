#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from pygame.sprite import Sprite
from pygame import Surface
from pygame import Rect
import pyganim

class Person(Sprite):

    def __init__(self, w, h, x, y, arr_anim, arr_anim2):
        Sprite.__init__(self)
        self.image = Surface((w, h))
        self.rect = Rect(0, 0, w, h)
        self.rect.x = x
        self.rect.y = y
        self.isSpeak = False
        self.isComment = True

        # Анимация персонаж стоит
        self.image.set_colorkey((0, 0, 40))
        self.persStay = pyganim.PygAnimation(arr_anim)
        self.persStay.play()

        # Анимация персонаж говорит
        self.persSpeak = pyganim.PygAnimation(arr_anim2)
        self.persSpeak.play()

    def anim(self):
        if self.isSpeak:
            self.image.fill((0, 0, 40))
            self.persSpeak.blit(self.image, (0, 0))
        else:
            self.image.fill((0, 0, 40))
            self.persStay.blit(self.image, (0, 0))
