from sprites import Animation
from root import Root

class Enemy(Animation):
    def __init__(S, step, size, pic, speed, track_list_in, lives=1, sounds=None):
        track_list = []
        for point in track_list_in:
            point_new = (int(point[0] * step[0] + step[0] / 2), int(point[1] * step[1] + step[1] / 2))
            track_list.append(point_new)
        print(track_list)
        size_new = (int(step[0] * size), int(step[1] * size))
        super().__init__(track_list[0], size_new, pic, 0.3, True, sounds)
        
        S.lives = lives
        S.speed = speed
        S.dir = 1
        S.points = []
        S.point = 0
        
        for segment in range(len(track_list) - 1):
            step_x_count = abs(track_list[segment][0] - track_list[segment + 1][0]) / S.speed
            step_y_count = abs(track_list[segment][1] - track_list[segment + 1][1]) / S.speed
            step_count = int(max(step_x_count, step_y_count))
            step_x = abs(track_list[segment][0] - track_list[segment + 1][0]) / step_count
            step_y = abs(track_list[segment][1] - track_list[segment + 1][1]) / step_count

            if track_list[segment][0] >= track_list[segment + 1][0]:
                step_x_dir = -1
            else:
                step_x_dir = 1
            
            if track_list[segment][1] >= track_list[segment + 1][1]:
                step_y_dir = -1
            else:
                step_y_dir = 1

            step_x_start = track_list[segment][0]
            step_y_start = track_list[segment][1]

            for _ in range(step_count):
                S.points.append((int(step_x_start), int(step_y_start)))
                step_x_start += step_x * step_x_dir
                step_y_start += step_y * step_y_dir

        S.points_len = len(S.points)
        
    def update(S):
        if S.point == S.points_len:
            S.point = S.points_len - 1
            S.dir = -1
        elif S.point < 0:
            S.point = 0
            S.dir = 1
        
        S.rect.center = S.points[S.point]
        S.point += S.dir
        super().update()

class Enemies(Root):
    def __init__(S, item_class):
        S.item_list = []
        S.item_class = item_class
        
    def load(S, enemy_list):
        S.backup = list(enemy_list)
        S.reset()

    def clear(S):
        S.item_list.clear()

    def reset(S):
        S.item_list.clear()
        for enemy in S.backup:
            # print(enemy)
            S.item_list.append(S.item_class(*enemy))
            # print(S.item_list)
        
    def kill(S, item):
        item.lives -= 1
        if item.lives == 0:
            item.sounds['death'].play()
            S.item_list.remove(item)
         
    def update(S):
        for item in S.item_list:
            item.update()
            

         
