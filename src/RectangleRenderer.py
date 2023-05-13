from src.Component import component

from pyray import *

from src.GameObject import gameObject
class rectangleRenderer(component):
    def __init__(self,
                 gameObject: gameObject,
                 position:Vector2=Vector2(0,0),
                 rotation:float=0,
                 name:str="Rectangle",
                 scale:Vector2=Vector2(1,1),
                 tint:Color=WHITE,
                 active:bool=True,
                 render_layer:int=0,
                 tag:str = None):

        self.render_layer = render_layer
        self.position = position
        self.rotation = rotation
        self.name = name
        self.scale = scale
        self.active = active
        self.components = []
        self.tag = tag
        self.tint = tint
        super().__init__(gameObject)
        self.tint = tint

    def render(self):
        draw_rectangle(int(self.position.x), int(self.position.y), int(self.scale.x), int(self.scale.y), RED)
        super().render()
