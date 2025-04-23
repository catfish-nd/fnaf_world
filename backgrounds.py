from sprites import GameSprite

class Background(GameSprite):
    def __init__(S):
        super().__init__((0, 0), (S.game.w, S.game.h), 'back')