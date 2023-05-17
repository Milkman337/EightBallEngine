from src.Component import component

from raypyc import *

from src.GameObject import gameObject

class spriteRenderer(component):
    def __init__(self, gameObject: gameObject,
                 sprite:str="None.png",
                 tint:Color=WHITE):
        super().__init__(gameObject)
        self.sprite_name = sprite
        self.sprite = load_texture("assets/"+self.sprite_name)
        self.tint = tint

    def render(self):
        draw_texture_pro(self.sprite,
                         Rectangle(0,0,self.sprite.width, self.sprite.height),
                         Rectangle(int(self.gameObject.position.x), int(self.gameObject.position.y), int(self.sprite.width*self.gameObject.scale.x), int(self.sprite.height*self.gameObject.scale.y)),
                         Vector2(int(self.sprite.width*self.gameObject.scale.x/2), int(self.sprite.height*self.gameObject.scale.y/2)),
                         self.gameObject.rotation,
                         self.tint)
        return super().render()
    
    def save(self):
        return {
            "sprite_name": self.sprite_name,
            "tint": self.tint
        }
    
    def load(self, data:dict):
        self.sprite_name = data["sprite_name"]
        self.tint = data["tint"]
        self.sprite = load_texture("assets/"+self.sprite_name)