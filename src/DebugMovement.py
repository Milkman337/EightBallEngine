from src.GameObject import gameObject
from src.Component import component

from raypyc import *

class debugMovement(component):
    def __init__(self, gameObject: gameObject,
                 speed:int = 10):
        self.gameObject = gameObject
        super().__init__(gameObject)
        self.speed = speed

    def update(self, dt: float):
        if is_key_down(KeyboardKey.KEY_UP):
            self.gameObject.position.y -= self.speed * dt
        if is_key_down(KeyboardKey.KEY_DOWN):
            self.gameObject.position.y += self.speed * dt
        if is_key_down(KeyboardKey.KEY_LEFT):
            self.gameObject.position.x -= self.speed * dt
        if is_key_down(KeyboardKey.KEY_RIGHT):
            self.gameObject.position.x += self.speed * dt
        return super().update(dt)
    
    def save(self):
        return {
            "speed": self.speed
        }
    
    def load(self, data:dict):
        self.speed = data["speed"]