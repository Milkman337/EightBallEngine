from raypyc import *
from src.Component import component
from src.GameObject import gameObject

class collider(component):
    def __init__(self, gameObject: gameObject,
                 collision_rec:Rectangle=Rectangle(-5,-5,10,10),
                 debug_render:bool=False):
        self.collision_rec = collision_rec
        self.gameObject = gameObject
        #TODO collider adding
        self.gameObject.scene.colliders.append(self)
        self.debug_render = debug_render
        super().__init__(gameObject)

    def save(self):
        return {
            "x": self.collision_rec.x,
            "y": self.collision_rec.y,
            "width": self.collision_rec.width,
            "height": self.collision_rec.height,
            "debug_render": self.debug_render
        }
    
    def load(self, data:dict):
        self.collision_rec = Rectangle(data["x"],
                                       data["y"],
                                       data["width"],
                                       data["height"])
        self.debug_render = data["debug_render"]

    def check_collision(self):
        #TODO check for a collision
        for col in self.gameObject.scene.colliders:
            if col == self or col.gameObject == self.gameObject:
                continue
            else:
                if check_collision_recs(Rectangle(int(self.gameObject.position.x+self.collision_rec.x*self.gameObject.scale.x),
                                                  int(self.gameObject.position.y+self.collision_rec.y*self.gameObject.scale.y),
                                                  self.collision_rec.width*self.gameObject.scale.x,
                                                  self.collision_rec.height*self.gameObject.scale.y),
                                        Rectangle(int(col.gameObject.position.x+col.collision_rec.x*col.gameObject.scale.x),
                                                  int(col.gameObject.position.y+col.collision_rec.y*col.gameObject.scale.y),
                                                  col.collision_rec.width*col.gameObject.scale.x,
                                                  col.collision_rec.height*col.gameObject.scale.y)):
                    return True, col.gameObject
    
    def render(self):
        if (self.debug_render):
            draw_rectangle_lines(int(self.gameObject.position.x+self.collision_rec.x*self.gameObject.scale.x),
                                 int(self.gameObject.position.y+self.collision_rec.y*self.gameObject.scale.y),
                                 int(self.collision_rec.width*self.gameObject.scale.x),
                                 int(self.collision_rec.height*self.gameObject.scale.y),
                                 MAROON)
        return super().render()