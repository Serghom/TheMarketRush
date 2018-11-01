#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import config
from pygame import mixer

music = 'music/'
sound = 'sound/'

mixer.pre_init(22050, -16, 1, 300)
mixer.init()



def playMusic():
    music_themarket = music + '1ac41fc1b0639d_pidoras.ogg'
    mixer.music.load(music_themarket)
    mixer.music.set_volume(config.vol)
    mixer.music.play(-1)


def checkPlayMusic():
    return mixer.music.get_busy()


def soundGlass():
    sound_glass = sound + 'glass.ogg'
    sound_glass = mixer.Sound(sound_glass)
    sound_glass.set_volume(config.vol)
    sound_glass.play()


def saysLuna1():
    says_Luna1 = sound + 'luna1.ogg'
    says_Luna1 = mixer.Sound(says_Luna1)
    says_Luna1.set_volume(config.vol)
    says_Luna1.play()


def saysLuna2():
    says_Luna2 = sound + 'luna2.ogg'
    says_Luna2 = mixer.Sound(says_Luna2)
    says_Luna2.set_volume(config.vol)
    says_Luna2.play()


def saysPlayer():
    says_nazar = sound + 'nazar1.ogg'
    says_nazar = mixer.Sound(says_nazar)
    says_nazar.set_volume(config.vol)
    says_nazar.play()
