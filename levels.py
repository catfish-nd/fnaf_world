import pygame as pg
import json
from root import Root

class Levels(Root):
    def __init__(S, **item_classes):
        S.item_classes = item_classes
        with open(S.app.levels_file, 'r', encoding='utf-8') as file:
            S.levels_files = json.load(file)
        S.levels = {}
        S.level = {}
        S.item_list = {}
        S.exits = []
        for level in S.levels_files['levels']:
            with open(level, 'r', encoding='utf-8') as file:
                data = json.load(file)
                S.levels[data['name']] = level
                
        # S.load(S.levels_files['begin'])
        # print(S.levels)

    def start(S):
        S.load(S.levels_files['begin'])
    
    def load(S, enter):
        S.level_file = S.levels[enter]
        S.level.clear()
        S.item_list.clear()
        S.exits.clear()

        with open(S.level_file, 'r', encoding='utf-8') as file:
            data = json.load(file)

        for name, value in data.items():
            S.level[name] = value
 
        S.level_w = S.level['size'][0]
        S.level_h = S.level['size'][1]
        S.level_x_step = S.game.w / S.level_w
        S.level_y_step = S.game.h / S.level_h
        
        for group, items in S.level['map'].items():
            S.item_list[items[0]] = [] 
            for item in items[2:]:
                if group in S.item_classes:
                    S.item_list[items[0]].append(S.item_classes[group]((int(item[0] * S.level_x_step), int(item[1] * S.level_y_step)), (int(S.level_x_step), int(S.level_y_step)), items[1]))
        
        if 'enemies' in S.level:
            enemy_list = []
            for enemy in S.level['enemies']:
                new = [(int(S.level_x_step), int(S.level_y_step))]
                new.append(enemy['size'])
                new.append(enemy['pic'])
                new.append(enemy['speed'])

                track_list = []
                for point in enemy['track']:
                    track_list.append(tuple(point))
                new.append(tuple(track_list))

                if 'lives' in enemy:
                    new.append(enemy['lives'])

                # new.append(enemy['lives'])
                new.append(enemy['snd'])

                enemy_list.append(tuple(new))
            S.game.objects.enemies.load(enemy_list)
        else:
            S.game.objects.enemies.clear()
        # print(enemy_list)

        # S.rect.center = (int(pos[0] + step[0] / 2), int(pos[1] + step[1] / 2))
        player_x = S.level['player'][0]
        player_y = S.level['player'][1]
        S.game.objects.player.start((int(S.level_x_step * player_x + S.level_x_step / 2), int(S.level_y_step * player_y + S.level_y_step / 2)))

        for exit in S.level['exits']:
            pos = (exit[0] * S.level_x_step, exit[1] * S.level_y_step)
            size = (S.level_x_step, S.level_y_step)
            S.exits.append(S.item_classes['exit'](pos, size, exit[2], exit[3]))
        
        S.layer_limit = max(list(S.item_list.keys())) + 1
        # print(S.level, "*" * 10)

            
    def update(S):
        S.game.screen.fill(S.level['back'])
        for layer in range(S.layer_limit):
            for item in S.item_list[layer]:
                item.update()
                # pass
        for exit in S.exits:
            exit.update()

if __name__ == '__main__':
    from root import App, Root
    from game import Game
    Root.app = App()
    Root.game = Game()
    class Dummy:
        def __init__(S, asdf):
            pass
    levels = Levels(
        # tree = Dummy
        )
    # print(levels.level)
    # print(levels.item_classes)
    # print(levels.item_list)
    