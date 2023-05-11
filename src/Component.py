from pyray import *
from src.GameObject import gameObject

class component:
    def __init__(self,
                 gameObject:gameObject):
        self.gameObject = gameObject
        self.gameObject.add_component(self)

    def update(self, dt:float):
        pass

    def render(self):
        pass