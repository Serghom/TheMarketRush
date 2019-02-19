#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from pygame.sprite import Sprite
from pygame import Surface
from pygame.key import get_pressed
from pygame import constants
from pygame import Rect
import animation
import pyganim


class Player(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = Surface((160, 230))
        self.rect = Rect(0, 0, 160, 230)
        self.reImage = self.image
        self.isRight = True
        self.isLeft = False
        self.isWalk = True
        self.isFinal = False
        self.isComment = True
        self.score = 0
        self.yvel = 0
        self.xvel = 0
        self.speedWalk = 5
        self.rect.x = x
        self.rect.y = y
        self.level = 0
        self.isTrigger = False
        self.isNonScore = False
        self.sneakersForce = 0
        self.isSneakersForce = False
        self.isSneakersTurn = True
        self.scene = 1

        self.image.set_colorkey((0, 0, 40))
        '''Анимация когда песонаж стоит'''
        self.AnimStay = pyganim.PygAnimation(animation.PLAYER_STAY)
        self.AnimStay.play()
        '''Анимация когда песонаж идет'''
        self.AnimWalk = pyganim.PygAnimation(animation.PLAYER_WALK)
        self.AnimWalk.play()

    def control(self):
        if self.scene == 1 and self.isWalk:
            self.xvel = self.speedWalk

        elif self.scene == 1 and not self.isWalk:
            self.xvel = 0

        elif self.scene == 2:
            # Блок отслеживания нажатия клавиш
            keys = get_pressed()
            # Если Зажата D или Стрелка вправо - идти вправо
            if (keys[constants.K_d] or keys[constants.K_RIGHT]) and self.rect.x < 1172:
                self.xvel = self.speedWalk
                self.isRight = True
                self.isLeft = False
                self.isWalk = True

            # Если Зажата A или Стрелка влево - идти влево
            if (keys[constants.K_a] or keys[constants.K_LEFT]) and self.rect.x > 55:
                self.xvel = -self.speedWalk
                self.isRight = False
                self.isLeft = True
                self.isWalk = True

        if self.isWalk:
            self.rect.x += self.xvel

        self.animPlayer()
        self.isWalk = False

    def animPlayer(self):
        # Определение стоит ли персонаж или нет
        if not self.isWalk:
            self.image.fill((0, 0, 40))
            self.AnimStay.blit(self.image, (0, 0))
        # Если не стоит то идет
        else:
            self.image.fill((0, 0, 40))
            self.AnimWalk.blit(self.image, (0, 0))
