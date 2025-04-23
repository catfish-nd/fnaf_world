import pygame as pg
from setup import Setup
from resources import Resources

class Root:
    pass

class App(Root, Setup, Resources):
    def __init__(S):
        pg.display.set_caption(S.title)
        S.clock = pg.time.Clock()
        S.events_list = []
        S.is_run = True
    
    def tick(S):
        S.clock.tick(S.FPS)
        pg.display.update()
        all_events = list(pg.event.get())
        if all_events:
            S.events_list = list(all_events)
        for e in S.events():
            if e.type == pg.QUIT:
                S.is_run = False
                break

    def event_remove(S, event):
        S.events_list.remove(event)

    def events(S):
        return S.events_list