from enum import IntEnum

class directions(IntEnum):
    STOP = 0
    RIGHT = 1
    LEFT = -1
    UP = 1
    DOWN = -1

class window(IntEnum):
    WIDTH = 600
    HEIGHT = 400

class angles(IntEnum):
    FACE_UP = 90
    FACE_DOWN = -90

TITLE = 'space invaders'
