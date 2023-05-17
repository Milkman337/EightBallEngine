from raypyc import *
from typing import Union
import simpleJDB
import os
#from src.Collider import collider

def sort_dict(dict:dict):
    in_list = []
    for g in dict.values():
        in_list.append(g)
    sorted_ = sorted(in_list, key=lambda x: x.render_layer)
    out = {}
    for g in sorted_:
        out[g.name] = g
    return out

class scene:
    def __init__(self, name:str="Scene",
                 active:bool=False,
                 background_color:Color=BLACK):
        self.name = name
        self.active:bool = active
        self.background_color = background_color
        self.gameobjects = {}
        self.save_db = simpleJDB.database(f"scenes/{self.name}")
        self.gameobjects = sort_dict(self.gameobjects)
        self.sorted = False
        from src.Collider import collider
        self.colliders:list[collider]=[]
        self.gameObjects_to_be_removed = []
        self.reset = False

        if os.path.exists(f'scenes/{self.name.replace(" ", "_")}.py'):
            exec(f"from scenes.{self.name.replace(' ', '_')} import SCENE")
            self.scene = eval(f"SCENE(self)")
        else:
            with open("src/scene_script_exmp.py", "r") as f:
                data = f.read()
            with open(f"scenes/{self.name.replace(' ', '_')}.py", "w") as f2:
                f2.write(data)
            exec(f"from scenes.{self.name.replace(' ', '_')} import SCENE")
            self.scene = eval(f"SCENE(self)")

    def add_gameObject(self, gameObject):
        i = 0
        while gameObject.name in self.gameobjects:
            i += 1
            gameObject.name = gameObject.name + str(i)
        self.gameobjects[gameObject.name] = gameObject
        self.gameobjects = sort_dict(self.gameobjects)

    def remove_gameObject(self, gameObject):
        for g in self.gameobjects.values():
            if g.name == gameObject.name:
                self.gameObjects_to_be_removed.append(gameObject.name)
                for c in self.colliders:
                    if c.gameObject == gameObject:
                        self.colliders.remove(c)

    def get_gameObject(self, gameObject:str):
        for g in self.gameobjects.values():
            if g.name == gameObject:
                return g
            
    def update(self, dt:float):
        if self.reset:
            self._reset_scene()
            self.reset = False
        if not self.sorted:
            self.gameobjects = sort_dict(self.gameobjects)
            self.sorted = True
        if self.active:
            gameObjects_clone = self.gameobjects.values()
            for i in range(len(gameObjects_clone)):
                list(self.gameobjects.values())[i].update(dt)
        for g in self.gameObjects_to_be_removed:
            del self.gameobjects[g]
            self.gameObjects_to_be_removed.remove(g)

    def render(self):
        if self.active:
            clear_background(self.background_color)
            for g in self.gameobjects.values():
                g.render()

    def _reset_scene(self):
        self.gameobjects.clear()
        self.colliders.clear()
        self.gameObjects_to_be_removed.clear()
        exec(f"from scenes.{self.name.replace(' ', '_')} import SCENE")
        self.scene = eval(f"SCENE(self)")

    def save(self):
        gameobjects = []
        for g in self.gameobjects.values():
            gameobjects.append(g.save())
        save_data = {
            "name": self.name,
            "active": self.active,
            "background_color": self.background_color,
            "gameobjects": gameobjects
        }
        self.save_db.setkey("scene", save_data)
        self.save_db.commit()

    def load(self):
        data = self.save_db.getkey("scene")

        self.name = data["name"]
        self.active = data["active"]
        self.background_color = data["background_color"]
        for g in data["gameobjects"]:
            from src.GameObject import gameObject
            a = gameObject(self).load(g)
        self.gameobjects = sort_dict(self.gameobjects)