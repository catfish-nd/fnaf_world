import pygame as pg
from root import Root
from random import randint
from sprites import Animation

class GameItem(pg.sprite.Sprite, Root):
    def __init__(S, pos, step, size, scale, rnd_pos, rnd_size, picture):
        super().__init__()
        if rnd_size:
            rnd_w = randint(int(size[0] * 0.8), int(size[0] * 1.2))
            rnd_h = randint(int(size[1] * 0.8), int(size[1] * 1.2))
            size = (rnd_w, rnd_h)
        S.image = pg.transform.scale(pg.image.load(S.app.files[picture]), (int(size[0] * scale), int(size[1] * scale)))
        S.rect = S.image.get_rect()
        if rnd_pos:
            rnd_x = int(abs(S.rect.w - step[0]) / 2) - 1
            rnd_y = int(abs(S.rect.h - step[1]) / 2) - 1
            S.rect.center = (int(pos[0] + step[0] / 2) + randint(-rnd_x, rnd_x), int(pos[1] + step[1] / 2) + randint(-rnd_y, rnd_y))
        else:
            S.rect.center = (int(pos[0] + step[0] / 2), int(pos[1] + step[1] / 2))
        
    def update(S):
        S.game.screen.blit(S.image, (S.rect.x, S.rect.y))
    




class Tree(GameItem):
    def __init__(S, pos, step, mode):
        super().__init__(pos, step, step, 0.7, True, True, 'tree')
        S.mode = mode

class Flower(GameItem):
    def __init__(S, pos, step, mode):
        super().__init__(pos, step, step, 0.7, False, False, 'flower')
        S.mode = mode

class Stump(GameItem):
    def __init__(S, pos, step, mode):
        super().__init__(pos, step, step, 0.7, True, True, 'stump')
        S.mode = mode
    
class SnowTree(GameItem):
    def __init__(S, pos, step, mode):
        super().__init__(pos, step, step, 0.7, True, True, 'snow_tree')
        S.mode = mode

class Cactus(GameItem):
    def __init__(S, pos, step, mode):
        super().__init__(pos, step, step, 0.7, True, False, 'cactus')
        S.mode = mode






class Exit(Root, pg.sprite.Sprite):
    def __init__(S, pos, step, dir, move_to):
        super().__init__()
        S.image = pg.transform.scale(pg.image.load(S.app.files['exit']), (int(step[0]), int(step[1])))
        S.move_to = move_to
        S.pos = pos
        S.rect = pg.Rect(pos, step)
        if dir == 'right': 
            right = S.rect.right
            S.rect.w *= 0.1
            S.rect.right = right
        if dir == 'down': 
            down = S.rect.bottom
            S.rect.h *= 0.1
            S.rect.bottom = down
        if dir == 'left': 
            S.image = pg.transform.flip(S.image, True, False)
            left = S.rect.left
            S.rect.w *= 0.1
            S.rect.left = left
        if dir == 'up': 
            up = S.rect.top
            S.rect.h *= 0.1
            S.rect.top = up

    def update(S):
        S.game.screen.blit(S.image, S.pos)
