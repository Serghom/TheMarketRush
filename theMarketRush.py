#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# TheMarketRush
# A game on Pygame.
#
# By Serghom serghom@shmeile.ru
# https://github.com/Serghom
# Released under a "MIT License"
__author__ = 'Serghom'


from initFunction import *

def mainFunction():
    # Камера
    class _Camera:
        def __init__(self, camera_func, width, height):
            self.camera_func = camera_func
            self.state = pygame.Rect(0, 0, width, height)

        def apply(self, target):
            return target.rect.move(self.state.topleft)

        def update(self, target):
            self.state = self.camera_func(self.state, target.rect)


    def camera_func(camera, target_rect):
        l = -target_rect.x + W / 2
        t = -target_rect.y + H / 2

        w, h = camera.width, camera.height

        l = min(0, l)
        l = max(-(camera.width - W), l)
        t = max(-(camera.height - H), t)
        t = min(0, t)

        return pygame.Rect(l, t, w, h)


    camera = _Camera(camera_func, 2048, 768)


    # Вывод информации на экран
    def info():
        screen.blit(font.render(u'Score: ' + str(player.score), 1, (255, 255, 255)), (55, 680))
        screen.blit(font.render(u' Level: ' + str(player.level), 1, (255, 255, 255)), (800, 680))
        screen.blit(status.render(u' Delay: ' + str(int(config.timeOfSpawn * 10)) + 'ms', 1, (255, 255, 255)),
                    (1200, 708))
        screen.blit(status.render(u' Speed: ' + str(player.speedWalk), 1, (255, 255, 255)), (1200, 738))
        screen.blit(status.render(u' Volume: ' + str(int(config.vol * 10)), 1, (255, 255, 255)), (1200, 650))
        if player.isFinal and not player.isNonScore:
            screen.blit(timerFont.render(str(int(config.startTime - time.time())), 1, (255, 255, 255)), (600, 680))
        if player.isNonScore:
            screen.blit(timerFont.render(u'WON' if player.score > 0 else u'Lost', 1, (255, 255, 255)), (580, 680))
            screen.blit(status.render(u'                  Press "Esc" to exit game' if player.score > 0
                                      else u'Fail, please try again. Press "Esc" to exit game', 1, (255, 255, 255)),
                        (370, 650))

    ### Инициализация ###
    W, H = variable()
    init_pygame()
    window, screen = create_surface(W, H)
    img_theMarket, img_street, img_adik, img_adikr = create_user_interface()

    # Таймер для фпс
    timer = pygame.time.Clock()

    font, status, timerFont, testFont = fonts()
    player, luna = create_person()


    # Группы спрайтов для отображения
    sprite_group_scene_1 = Group()
    sprite_group_scene_2 = Group()
    sprite_group_loot = Group()

    add_sprite_group(sprite_group_scene_1, sprite_group_scene_2,
                     img_street, player, img_theMarket,
                     img_adik, img_adikr, luna)

    # Массив объектов для проверки столкновений
    collision = []

    # Таймер для анимации разговора
    config.speakTime = time.time() + 5

    # Выключаем мышку
    pygame.mouse.set_visible(0)

    # Основной цикл
    done = True
    while done:
        # Блок отслеживания кнопки закрыть
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                done = False
            # Блок отслеживания нажатия клавш
            if e.type == pygame.KEYDOWN:
                # Отключаем дубликацию
                pygame.key.set_repeat(1, 1)
                # Отслеживание клавиги ESCAPE
                if e.key == pygame.K_ESCAPE:
                    done = False
                # if e.key == pygame.K_s:
                #     player.score += 1000
                # if e.key == pygame.K_f:
                #     player.sneakersForce += 10
                #     config.rectCounter -= 140
                if e.key == pygame.K_DOWN:
                    if config.vol - .1 >= 0:
                        config.vol -= .1
                    mixer.music.set_volume(config.vol)
                if e.key == pygame.K_UP:
                    if config.vol + .1 <= 1:
                        config.vol += .1
                    mixer.music.set_volume(config.vol)

        if player.scene == 1:
            scene1(screen, player,
                   camera, sprite_group_scene_1)

        elif player.scene == 2:
            scene2(screen, player, luna,
                   collision, sprite_group_scene_2,
                   sprite_group_loot, camera)
            info()

        window.blit(screen, (0, 0))
        # Обновляем окно
        pygame.display.flip()
        timer.tick(120)

    # write_log_close_game(player.level, player.score)
    pygame.quit()

mainFunction()

