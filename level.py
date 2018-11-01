#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from log import write_log
import config
# Взависимости от очков усложняется игра
def level(player):
    if not player.isFinal:
        if -1 < player.score < 50:
            if player.level != 1:
                write_log(1, player.score)
            config.timeOfSpawn = .5
            player.speedWalk = 7
            player.level = 1

        elif 49 < player.score < 150:
            if player.level != 2:
                write_log(2, player.score)
            config.timeOfSpawn = .4
            player.speedWalk = 9
            player.level = 2

        elif 149 < player.score < 300:
            if player.level != 3:
                write_log(3, player.score)
            config.timeOfSpawn = .3
            player.speedWalk = 12
            player.level = 3

        elif 299 < player.score < 1000:
            if player.level != 4:
                write_log(4, player.score)
            config.timeOfSpawn = .2
            player.speedWalk = 15
            player.level = 4

        elif 999 < player.score:
            player.isFinal = True
            if player.level != 5:
                write_log(5, player.score)
            config.timeOfSpawn = .01
            player.speedWalk = 4
            player.level = 5

