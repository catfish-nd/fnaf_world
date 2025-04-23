import pygame as pg
from root import Root

class Label(Root):
    def __init__(S, pos, color, size):
        S.pos = pos
        S.color = color
        S.font = pg.font.SysFont("Arial", size)
        if not isinstance(S.pos, tuple):
            S.line, S.lines = tuple(map(int, S.pos.split('/')))
            S.pos_flag = True 
        else:
            S.pos_flag = False
        S.surface = None

    def setText(S, text = ' '):
        S.surface = S.font.render(text, True, S.color)
        if S.pos_flag:
            S.x = int(S.game.w / 2 - S.surface.get_width() / 2)
            S.y = int((S.game.h / S.lines) * S.line - S.surface.get_height() / 2)
            
    def update(S):
        if S.surface != None:
            if S.pos_flag:
                S.game.screen.blit(S.surface, (S.x, S.y))
            else:
                S.game.screen.blit(S.surface, S.pos)