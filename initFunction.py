#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import pygame
import time
import animation
import config
from pygame import mixer
from pygame.sprite import Group
from background import World
from player import Player
from personage import Person
from log import write_log_close_game
from scene import scene1, scene2


def variable():
    # Размер окна
    W, H = 1366, 768
    # Время для спавна
    config.dropCounter = time.time()
    # Как часто будут спавнится
    config.timeOfSpawn = .5
    # Таймер в конце игры
    config.startTime = 0
    # Таймер для "волны дропа"
    config.sneakersForceTime = 0
    # Координаты спавна "волны дропа" и его id
    config.masSpawnDrop = list(range(56, 1170, 70))
    config.masCounter = 0
    # Сила "волны дропа"
    config.rectCounter = 1366
    # Таймер начала игры
    config.startGameTime = time.time()
    # Громкость
    config.vol = .3

    return W, H


def init_pygame():
    # Инициализация пайма
    pygame.init()
    # Инициализация текста
    pygame.font.init()
    # Инициализируем звуковое устройство
    mixer.init()


def create_surface(W, H):
    # создание окна и скрина
    window = pygame.display.set_mode((W, H), pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF)
    screen = pygame.Surface((W, H))
    return window, screen


def create_user_interface():
    # Загружаем картинку и переделываем ей нужные нам размеры
    img_theMarket = World('backgraund/themarket.png', 0, 128, 0, 0, 1366, 512)
    img_street = World('backgraund/street.png', 0, 0, 0, 0, 1366, 768)
    img_adik = World('backgraund/adik.png', 53, 0, 0, 0, 630, 128)
    img_adikr = World('backgraund/adik.png', 684, 0, 0, 0, 630, 128)
    # Создаем 2-мерный массив ar adikr
    ar = pygame.PixelArray(img_adikr.image)
    # Переворачиваем массив по Y '(каждой строчке массива начиная с первой Ymin+1 ar[:]
    # присваиваем значение строчки начиная с последней Ymax-1 ar[:,::-1]) '
    ar[:] = ar[::-1, :]
    del ar
    return img_theMarket, img_street, img_adik, img_adikr


def fonts():
    # Настройка шрифта
    font = pygame.font.SysFont('Calibri', 100, 1, 1)
    status = pygame.font.SysFont('Calibri', 30, 1, 1)
    timerFont = pygame.font.SysFont('Calibri', 100, 1, 1)
    testFont = pygame.font.SysFont('Calibri', 10, 1, 1)
    return font, status, timerFont, testFont


def create_person():
    # Персонаж
    player = Player(-160, 450)  # 55, 450
    luna = Person(154, 100, 1190, 470, animation.STAY_LUNA, animation.SPEAK_LUNA)
    return player, luna


def add_sprite_group(sprite_group_scene_1, sprite_group_scene_2,
                     img_street, player, img_theMarket,
                     img_adik, img_adikr, luna):
    # Добовляем в группу спрайтов фон и персонажа
    sprite_group_scene_1.add(img_street)
    sprite_group_scene_1.add(player)

    sprite_group_scene_2.add(img_theMarket)
    sprite_group_scene_2.add(img_adik)
    sprite_group_scene_2.add(img_adikr)
    sprite_group_scene_2.add(luna)
    sprite_group_scene_2.add(player)

    return sprite_group_scene_1, sprite_group_scene_2
