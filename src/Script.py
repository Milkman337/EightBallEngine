from pyray import *
from src.Component import component
from src.GameObject import gameObject

class script(component):
    def __init__(self, gameObject: gameObject,
                 script):
        self.gameObject = gameObject
        self.script = script
        self.script.gameObject = self.gameObject
        print(self.script)
        super().__init__(gameObject)

    def update(self, dt: float):
        self.script.update(dt)
        return super().update(dt)

    def render(self):
        self.script.render()
        return super().render()