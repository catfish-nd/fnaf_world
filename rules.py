from root import Root

class Rules(Root):
    def __init__(S):
        S.lives = 10
        S.enemy_count = 0

    def check(S):
        if S.lives == 0:
            S.game.mode = 2
        elif S.enemy_count == 0:
            S.game.mode = 1