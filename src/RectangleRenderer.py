from src.Component import component

from pyray import *

from src.GameObject import gameObject
class rectangleRenderer(component):
    def __init__(self,
                 gameObject: gameObject,
                 scale: Vector2=Vector2(1,1),
                 Color:Color=WHITE):

        self.Color = Color
        self.scale = scale
        super().__init__(gameObject)

    def render(self):
        draw_rectangle_pro(
            Rectangle(int(self.gameObject.position.x), int(self.gameObject.position.y), int(self.scale.x), int(self.scale.y)),
            Vector2(self.scale.x/2, self.scale.y/2),
            self.gameObject.rotation,
            self.Color
        )
        super().render()
