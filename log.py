#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import base64
import time
import config


def write_log(level, score):
    try:
        file = open('log/game.log', 'a')
    except IOError:
        file = open('log/game.log', 'w')
    game_time = time.time() - config.startGameTime
    write = time.asctime() + ' | ' + str(int(game_time/60)) + ':' + str(int(game_time % 60))
    write += ' | ' + str(level) + ' | ' + str(score) + '\n'
    file.write(encode(write) + '\n')
    file.close()


def write_log_close_game(level, score):
    try:
        file = open('log/game.log', 'a')
    except IOError:
        file = open('log/game.log', 'w')
    game_time = time.time() - config.startGameTime
    write = time.asctime() + ' | ' + str(level) + ' | ' + str(score) + ' Exit\n'
    if level == 5:
        write += 'Results: WON\n' if score > 0 else 'Full game: Lost\n'
    write += 'Time in game: ' + str(int(game_time/60)) + ':' + str(int(game_time % 60)) + '\n'
    write += '=-=-=-=-=-=-=Exit Game=-=-=-=-=-=-=\n'
    file.write(encode(write) + '\n')
    file.close()


def encode(string):
    string = bytes("""{}""".format(string), 'UTF-8')
    string = base64.b64encode(string)
    string = str(string, 'UTF-8')
    return string
