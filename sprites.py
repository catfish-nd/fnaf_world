import pygame as pg
from root import Root

class GameSprite(pg.sprite.Sprite, Root):
    def __init__(S, pos, size, picture):
        super().__init__()
        S.image = pg.transform.scale(pg.image.load(S.app.files[picture]), size)
        S.rect = S.image.get_rect()
        S.rect.x, S.rect.y = pos

    def update(S):
        S.game.screen.blit(S.image, (S.rect.x, S.rect.y))

class Animation(pg.sprite.Sprite, Root):
    from time import time
    
    def __init__(S, pos, size, picture, delay, loop, sounds=None):
        print(pos, size, 20 * "*")
        super().__init__()
        S.frames = []
        S.frame = 0
        for pic in S.app.files[picture]:
            S.frames.append(pg.transform.scale(pg.image.load(pic), size))
        S.frames_len = len(S.frames) - 1
        S.rect = S.frames[1].get_rect()
        S.rect.center = pos
        if sounds != None:
            S.sounds = {}
            for key in S.app.files[sounds]:
                S.sounds[key] = pg.mixer.Sound(S.app.files[sounds][key])
        S.delay = delay
        S.loop = loop
        S.loop_end = False
        S.delay_start = Animation.time()

    def update(S):
        if not S.loop_end:
            if Animation.time() - S.delay_start >= S.delay:
                if S.frame < S.frames_len:
                    S.frame += 1
                else:
                    if not S.loop:
                        S.loop_end = True
                    else:
                        S.frame = 0
                S.delay_start = Animation.time()
        S.game.screen.blit(S.frames[S.frame], (S.rect.x, S.rect.y))
