#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import pygame
import time
import config
from pygame.sprite import collide_rect
from pygame.transform import rotate
from pygame.mixer import get_busy
from random import randint
from loot import Drop
from level import level
from music_and_sound import playMusic
from music_and_sound import soundGlass
from music_and_sound import saysPlayer
from music_and_sound import saysLuna1
from music_and_sound import saysLuna2
from music_and_sound import checkPlayMusic

# ok google: python style guide
# CamelCase camelCaseAgain
# snake_case SNAKE_CASE


def scene1(screen, player,
           camera, sprite_group):

    # obladaet.isWalk
    if player.isComment:
        player.isWalk = True

    # Если разговорное время не вышло и персонаж находится на нужных координатах
    if player.isComment and player.rect.x > 900:
        # Останавливаем персонажа
        player.isWalk = False
        if not get_busy() and player.isComment:
            player.isComment = False
            saysPlayer()
            config.speakTime = time.time() + .3


    # Когда время закончилось, запускаем персонажа в "полет"
    elif player.rect.x > 900 and not get_busy() and not config.isJump:
        config.rotatePlayer -= 1
        player.rect.y -= 26
        player.image = rotate(player.image, config.rotatePlayer)
        if config.rotatePlayer < -10:
            config.isJump = True

    # Как только персонаж долетел до границы экрана,
    # включаем звук стекла и красим экран в черный
    elif config.isJump and not config.blackScreen:
        soundGlass()
        config.blackScreen = True

    # Сценарий перехода на следуюшую сцену
    elif not get_busy() and player.rect.x > 900:
        player.scene = 2
        player.image = player.reImage
        # Таймер для анимации разговора
        config.speakTime = time.time() + 5
        # Устанавливаем координаты персонажа
        player.rect.x, player.rect.y = 55, 450

    if not config.blackScreen:
        for e in sprite_group:
            screen.blit(e.image, camera.apply(e))
    else:
        screen.fill((0, 0, 0))

    player.control()


def scene2(screen, player, luna,
            collision, sprite_group,
            sprite_group_loot, camera):

    # Закрашиваем фон в черный
    screen.fill((0, 0, 0))

    # Проверяем говорит ли персонаж Luna
    luna.isSpeak = config.speakTime >= time.time()
    if not get_busy() and luna.isSpeak:
        if luna.isComment:
            saysLuna1()
            luna.isComment = False
        else:
            saysLuna2()

    if not luna.isSpeak and not checkPlayMusic():
        # Включаем музыку
        playMusic()

    # Если не выключен подсчет очков и не включена "волна дропа" то:
    if not player.isNonScore and not player.isSneakersForce and not luna.isSpeak:
        # Если прошло достаточно времени для то:
        if time.time() - config.dropCounter > config.timeOfSpawn:
            # Обновляем время
            config.dropCounter = time.time()
            # Создаем экземпляр класса
            drop = Drop(randint(56, 1170), 200)
            # Помещаем экземпляр класса в массив для проверки столкновений
            collision.append(drop)
            # Помещаем экземпляр класса в группу спрайтов
            sprite_group_loot.add(drop)

    # Если очков достаточно для "волны дропа" и финал выключен
    if player.sneakersForce >= 100 and not player.isFinal and not luna.isSpeak:
        # Даем 10 секунд
        config.sneakersForceTime = time.time() + 10
        # Сбрасываем силу волны
        player.sneakersForce = 0
        # Включаем "волну дропа"
        player.isSneakersForce = True

    # Если "волна дропа" включена и выключен финал
    if player.isSneakersForce and not player.isFinal:
        # Если времени с момента придедущего спавно прошло достаточно
        if time.time() - config.dropCounter > .15:
            # Если указатель выходит за пределы массива
            if config.masCounter + 1 > len(config.masSpawnDrop) - 1:
                # Разварачиваем "волну дропа" налево
                player.sneakersTurn = True
            # Если указатель выходит за пределы массива
            if config.masCounter - 1 < 0:
                # Разварачиваем "волну дропа" направо
                player.sneakersTurn = False

            # Смотрим в какую сторону повернута волна и меняем указатель
            if player.sneakersTurn:
                config.masCounter -= 1
            else:
                config.masCounter += 1

            # Есил время "волны" прошло, то выключаем ее
            if time.time() - config.sneakersForceTime > 0:
                player.isSneakersForce = False
            # Обновляем счетчик
            config.dropCounter = time.time()
            # Создаем экземпляр класса
            drop = Drop(config.masSpawnDrop[config.masCounter], 200)
            collision.append(drop)
            sprite_group_loot.add(drop)
            # Отображение силы сверху
            if config.rectCounter + 1366 / 50 > 1366:
                config.rectCounter = 1366
            else:
                config.rectCounter += 1366 / 50

    # Отображаем всю группу спрайтов
    for e in sprite_group:
        screen.blit(e.image, camera.apply(e))

    # Сила "волны дропа"
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, config.rectCounter, 128))

    # Отображаем группу спрайтов для дропа
    for e in sprite_group_loot:
        Drop.gravity(e)
        screen.blit(e.image, camera.apply(e))

        # Проверка на столконовения героя с обьектами
        if collide_rect(player, e):
            # Если не выключен подсчет очков
            if not player.isNonScore:
                # Если включен финал
                if player.isFinal and not luna.isSpeak:
                    player.score += 8
                else:
                    player.score += 1
                # Если не включена "волна дропа"
                if not player.isSneakersForce:
                    if config.rectCounter - 14 > 0:
                        config.rectCounter -= 14
                    player.sneakersForce += 1
            # Удаляем экземпляр класса
            sprite_group_loot.remove(e)

        if e.rect.y > 570 :
            if not player.isNonScore and not luna.isSpeak:
                if player.isFinal:
                    player.score -= 7
                elif not luna.isSpeak:
                    player.score -= 1
            sprite_group_loot.remove(e)

    # Есди включен финал
    if player.isFinal:
        # Если не вкдючен тригер даем игроку 30 сек
        if not player.isTrigger:
            currentTimestamp = time.time()
            config.speakTime = currentTimestamp + 7
            config.startTime = currentTimestamp + 37
            player.isSneakersForce = False
            player.sneakersForse = 0
            player.isTrigger = True
        if config.startTime <= time.time():
            player.isNonScore = True

    # Управление персонажем
    player.control()

    luna.anim()
    level(player)
