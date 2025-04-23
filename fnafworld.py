import pygame as pg

pg.init()
from root import Root, App
from game import Game
from rules import Rules
from labels import Label
# from enemies import Enemy, Enemies 
from backgrounds import Background
from levels import Levels
from game_items import Tree, Flower, Exit, Stump, SnowTree, Cactus
from player import Player
from enemies import Enemy, Enemies
from shoots import Shoot, Shoots


Root.app = App()
Root.game = Game()
Root.rules = Rules()
app = Root.app

label_win = Label('1/2', app.colors['text'], 120)
label_win.setText(app.texts['win'])
label_lose = Label('1/2', app.colors['text'], 110)
label_lose.setText(app.texts['lose'])
label_lives = Label((10, 10), app.colors['stat'], 30)

# app.game.objects.background = Background()
app.game.objects.levels = Levels(flower=Flower, tree=Tree, exit=Exit, stump=Stump, snow_tree=SnowTree, cactus=Cactus)
app.game.objects.player = Player()
app.game.objects.enemies = Enemies(Enemy)
# test = Enemy(
#     (50, 50),
#     'enemy',
#     [(1, 1), (6, 6)]
# )
app.game.objects.shoots = Shoots(Shoot)

app.game.objects.levels.start()


while app.is_run:
    # app.rules.check()
    if app.game.mode == 0:
        # main.screen.fill(main.colors['back'])
        app.game.action()
        app.game.update()

        # label_lives.setText(app.texts['lives'] + str(app.rules.lives))
        # label_lives.update()
        # label_bonus.setText(bonuses.mode_message)
        # label_bonus.update()

    elif app.game.mode == 1:
        app.game.screen.fill(app.colors['back_win'])
        label_win.update()
    elif app.game.mode == 2:
        app.game.screen.fill(app.colors['back_lose'])
        label_lose.update()
    elif app.game.mode == 3:
        pass
    app.tick()
