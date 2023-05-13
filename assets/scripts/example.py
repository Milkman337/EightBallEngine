from pyray import *
from src.GameObject import gameObject

class example_script:
    def __init__(self):
        self.gameObject:gameObject = None # this will be set automatically

    def update(self, dt:float):
        pass

    def render(self):
        pass