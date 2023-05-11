from pyray import *
from src.Scene import scene

class gameObject:
    def __init__(self,
                 scene:scene,
                 position:Vector2=Vector2(0,0),
                 rotation:float=0,
                 name:str="GameObject",
                 scale:Vector2=Vector2(1,1),
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
        self.scene = scene
        self.tag = tag
        self.scene.add_gameObject(self)

    def get_component(self, component_name:str):
        for com in self.components:
            if type(com).__name__ == component_name:
                return com

    def add_component(self, component):
        self.components.append(component)

    def remove_component(self, component):
        self.components.remove(component)

    def update(self, dt:float):
        if self.active:
            for c in self.components:
                c.update(dt)

    def render(self):
        if self.active:
            for c in self.components:
                c.render()

    def save(self):
        components = []
        component_saves = []
        for c in self.components:
            components.append(type(c).__name__)
            if (hasattr(type(c), "save")):
                component_saves.append({
                    "component_name": type(c).__name__,
                    "data": c.save()
                })
        save_data = {
            "position": [self.position.x, self.position.y],
            "rotation": self.rotation,
            "name": self.name,
            "scale": [self.scale.x, self.scale.y],
            "active": self.active,
            "components": components,
            "component_saves": component_saves,
            "render_layer": self.render_layer
        }
        return save_data
    
    def load(self, data:dict):
        self.position = Vector2(data["position"][0], data["position"][1])
        self.rotation = data["rotation"]
        self.name = data["name"]
        self.scale = Vector2(data["scale"][0], data["scale"][1])
        self.active = data ["active"]
        self.render_layer = data["render_layer"]
        for c in data["components"]:
            exec(f"from src.{c[0].upper()+c[1:]} import {c}")
            comp = eval(f"{c}(self)")
            
            if hasattr(type(comp), "load"):
                for a in data["component_saves"]:
                    if a["component_name"] == c:
                        comp.load(a["data"])
