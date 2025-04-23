from root import Root
import pygame as pg
from time import time

class Player(Root, pg.sprite.Sprite):
    def __init__(S):
        super().__init__()
        size = (70, 70)
        S.steps = {}
        
        for dir in ['up', 'right', 'down', 'left']:
            S.steps[dir] = {
                'pics': [],
                'len': 0
            }
            for step in S.app.files['player'][dir]:
                S.steps[dir]['pics'].append(pg.transform.scale(pg.image.load(step), size))
            S.steps[dir]['len'] = len(S.steps[dir]['pics']) 

        S.rect = S.steps['up']['pics'][0].get_rect()
        S.rect.x, S.rect.y = 0, 0
        S.delay = 0.06
        S.speed = 10
        S.sounds = {}
        for key in S.app.files['player_snd']:
            S.sounds[key] = pg.mixer.Sound(S.app.files['player_snd'][key])
        # S.start()
    
    def start(S, pos, dir=None):
        S.pos = pos
        S.dir = dir
        if dir == None:
            S.dir = 'right'
        S.reset()

    def reset(S):
        S.rect.center = S.pos
        S.speed_x, S.speed_y = 0, 0
        S.delay_start = time()
        S.frame = 0
        S.move_flag = False
    
    def step(S):
        if S.move_flag:
            if time() - S.delay_start >= S.delay:
                S.delay_start = time()
                S.frame += 1
                if S.frame == S.steps[S.dir]['len']:
                    S.frame = 0

    def action(S):
        S.step()
        S.move()
        S.fire()
        S.touch()

    def move(S):
        for e in S.app.events():
            if e.type == pg.KEYDOWN:
                S.move_flag = True

                if e.key == pg.K_LEFT:
                    S.speed_x = -1
                    S.dir = 'left'
                elif e.key == pg.K_RIGHT:
                    S.speed_x = 1
                    S.dir = 'right'
                
                if e.key == pg.K_UP:
                    S.speed_y = -1
                    S.dir = 'up'
                elif e.key == pg.K_DOWN:
                    S.speed_y = 1
                    S.dir = 'down'
                
            elif e.type == pg.KEYUP:
                if e.key in [pg.K_LEFT, pg.K_RIGHT]:
                    S.speed_x = 0
                
                if e.key in [pg.K_UP, pg.K_DOWN]:
                    S.speed_y = 0
                
                if not (S.speed_x or S.speed_y):
                    S.move_flag = False

        if S.speed_x != 0:
            for _ in range(S.speed):
                S.rect.x += S.speed_x
                for exit in S.game.objects.levels.exits:
                    if pg.sprite.collide_rect(S, exit):
                        dir = S.dir
                        S.game.objects.levels.load(exit.move_to)
                        S.dir = dir
                        break

                if S.rect.left < 0:
                    S.rect.left = 0
                    break
                
                if S.rect.right > S.game.w:
                    S.rect.right = S.game.w
                    break

                for layer in range(S.game.objects.levels.layer_limit):
                    for item in S.game.objects.levels.item_list[layer]:
                        if item.mode == 1:
                            if pg.sprite.collide_rect(S, item):
                                S.rect.x -= S.speed_x
                                break
                        
        if S.speed_y != 0:
            for _ in range(S.speed):
                S.rect.y += S.speed_y
                for exit in S.game.objects.levels.exits:
                    if pg.sprite.collide_rect(S, exit):
                        dir = S.dir
                        S.game.objects.levels.load(exit.move_to)
                        S.dir = dir
                        break

                if S.rect.top < 0:
                    S.rect.top = 0
                    break
                
                if S.rect.bottom > S.game.h:
                    S.rect.bottom = S.game.h
                    break
                

                for layer in range(S.game.objects.levels.layer_limit):
                    for item in S.game.objects.levels.item_list[layer]:
                        if item.mode == 1:
                            if pg.sprite.collide_rect(S, item):
                                S.rect.y -= S.speed_y
                                break 

    def fire(S):
        for event in S.app.events():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    S.app.event_remove(event)
                    S.game.objects.shoots.new(S.rect, S.dir)
                    break 

    def touch(S):
        for enemy in S.game.objects.enemies.item_list:
            if pg.sprite.collide_rect(S, enemy):
                S.sounds['death'].play()
                S.game.objects.enemies.reset()
                S.reset()
    
    def update(S):
        S.game.screen.blit(S.steps[S.dir]['pics'][S.frame], (S.rect.x, S.rect.y))
        # print(S.rect.center, S.right)

    