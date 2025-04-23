import pygame as pg
from root import Root
from setup import Setup

class Game(Root, Setup):
    def __init__(S):
        S.mode = 0
        S.objects = S.Objects()
        S.screen = pg.display.set_mode((S.w, S.h))
    
    class Objects:
        pass

    def action(S):
        for obj in vars(S.objects).values():
            if hasattr(obj, 'action'):
                obj.action()
    
    def update(S):
        for obj in vars(S.objects).values():
            obj.update()