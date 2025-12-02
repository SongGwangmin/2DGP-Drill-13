from pico2d import *
import game_world
import game_framework
import random
import common

class Ball:
    image = None

    def __init__(self, x = None, y = None):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x = x if x else random.randint(21, common.court.w - 1 - 21)
        self.y = y if y else random.randint(21, common.court.h - 1 - 21)

    def draw(self):
        sx = self.x - common.court.window_left
        sy = self.y - common.court.window_bottom
        self.image.draw(sx, sy)
        draw_rectangle(*self.get_windowbb())

    def update(self):
        pass

    def get_windowbb(self):
        sx = self.x - common.court.window_left
        sy = self.y - common.court.window_bottom
        return sx - 10, sy - 10, sx + 10, sy + 10

    def get_bb(self):
        
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self, group, other):
        match group:
            case 'boy:ball':
                game_world.remove_object(self)