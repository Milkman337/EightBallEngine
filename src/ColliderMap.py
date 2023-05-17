from src.GameObject import gameObject
from src.Component import component
from src.Collider import collider
import simpleJDB

from raypyc import *

class colliderMap(component):
    def __init__(self, gameObject: gameObject,
                 collider_map_name:str="colliders"):
        self.gameObject = gameObject
        self.collider_map_name = collider_map_name
        self.save_data = simpleJDB.database(f"assets/level/{self.collider_map_name}")
        self.collider_list:list[dict] = self.save_data.getkey("colliders")
        for c in self.collider_list:
            self.gameObject.add_component(collider(self.gameObject, Rectangle(c["x"], c["y"], c["width"], c["height"]), True))
        super().__init__(gameObject)