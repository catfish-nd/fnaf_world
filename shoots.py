import pygame as pg
from sprites import Animation
from root import Root

class Shoot(Animation):
    def __init__(S, rect, dir):
        super().__init__(rect.center, (40, 40), 'shoot', 0.05, True, 'shoot_snd')
        if dir == 'right':
            S.speed_x = 1
            S.speed_y = 0
            S.rect.left, S.rect.centery = rect.right, rect.centery
        elif dir == 'down':
            S.speed_x = 0
            S.speed_y = 1
            S.rect.centerx, S.rect.top = rect.centerx, S.rect.bottom
        elif dir == 'left':
            S.speed_x = -1
            S.speed_y = 0
            S.rect.right, S.rect.centery = rect.left, rect.centery
        elif dir == 'up':
            S.speed_x = 0
            S.speed_y = -1
            S.rect.centerx, S.rect.bottom = rect.centerx, rect.top
        
        S.visible = True
        S.speed = 15
        S.sounds['fire'].play()

    def update(S):
        super().update()
        S.rect.x += S.speed * S.speed_x
        S.rect.y += S.speed * S.speed_y
        if S.rect.right < 0 or S.rect.left > S.game.w or S.rect.bottom < 0 or S.rect.top > S.game.h:
            S.visible = False



class Shoots(Root):
    def __init__(S, item_class):
        S.item_class = item_class
        S.item_list = []
        S.reset()

    def action(S):
        S.hit()

    def reset(S):
        S.item_list.clear()

    def new(S, pos, dir):
        S.item_list.append(S.item_class(pos, dir))

    def hit(S):
        for item in S.item_list:
            for layer in range(S.game.objects.levels.layer_limit):
                for layer_item in S.game.objects.levels.item_list[layer]:
                    if layer_item.mode == 1:
                        if pg.sprite.collide_rect(item, layer_item):
                            S.item_list.remove(item)
                            break

        for item in S.item_list:
            for enemy in S.game.objects.enemies.item_list:
                if pg.sprite.collide_rect(item, enemy):
                    S.item_list.remove(item)
                    S.game.objects.enemies.kill(enemy)
                    break

    def update(S):
        for item in S.item_list:
            item.update()
            if not item.visible:
                S.item_class.remove(item)





        