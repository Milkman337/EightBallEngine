from pyray import *
from GameObject import gameObject
from src.GameObject import gameObject
from src.Component import component

class particleSystem(component):
    def __init__(self, gameObject: gameObject):
        self.gameObject:gameObject = gameObject
        super().__init__(gameObject)

    def update(self, dt: float):
        return super().update(dt)
    
    def render(self):
        return super().render()