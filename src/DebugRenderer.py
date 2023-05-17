from src.Component import component
from src.GameObject import gameObject

from raypyc import *

class debugRenderer(component):
    def __init__(self, gameObject: gameObject):
        super().__init__(gameObject)

    def render(self):
        draw_rectangle(int(self.gameObject.position.x), int(self.gameObject.position.y), 10, 10, RED)
        return super().render()
