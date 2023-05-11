from pyray import *
from src.Component import component
from src.GameObject import gameObject
import simpleJDB
from typing import TypedDict

class Tile:
    def __init__(self, x, y, texture, texture_name):
        self.x = x
        self.y = y 
        self.texture = texture
        self.texture_name = texture_name

    def from_dict(self, data: dict):
        self.x = data["x"]
        self.y = data["y"]
        self.texture_name = data["texture_name"]
        self.texture = load_texture(self.texture_name)

class TileDict(TypedDict):
    x: int
    y: int
    texture_name: str

class RoomDict(TypedDict):
    offset_x: float
    offset_y: float
    width: int
    height: int
    tiles: list[TileDict]

class Room(TypedDict):
    texture:RenderTexture2D
    offset: Vector2

class spriteMap(component):
    def __init__(self, gameObject: gameObject,
                 map_name:str="data"):
        super().__init__(gameObject)
        self.map_name = map_name
        self.save_data = simpleJDB.database("assets/level/" + self.map_name)
        self.rooms: list[RoomDict] = []
        for r in self.save_data.getkey("level"):
            self.rooms.append(r)
        self.baked_rooms: list[Room] = []
        print(self.rooms)
        for r in self.rooms:
            new_texture: RenderTexture2D = load_render_texture(r["width"], r["height"])
            for t in r["tiles"]:
                tile_texture: Texture2D = load_texture("assets/" + t["texture_name"])
                begin_texture_mode(new_texture)
                draw_texture(tile_texture, int(t["x"]-r["offset_x"]), int(t["y"]-r["offset_y"]), WHITE)
                end_texture_mode()
            self.baked_rooms.append({
                "texture": new_texture,
                "offset": Vector2(r["offset_x"], r["offset_y"])
            })
        print(self.baked_rooms)

    def render(self):
        for r in self.baked_rooms:
            draw_texture_pro(r["texture"].texture,
                             Rectangle(0,0,r["texture"].texture.width,-r["texture"].texture.height),
                             Rectangle(int(self.gameObject.position.x+r["offset"].x*self.gameObject.scale.x), int(self.gameObject.position.y+r["offset"].y*self.gameObject.scale.y), r["texture"].texture.width*self.gameObject.scale.x, r["texture"].texture.height*self.gameObject.scale.y),
                             Vector2(0,0),
                             self.gameObject.rotation,
                             WHITE)
        return super().render()

    def save(self):
        return {
            "map_name": self.map_name
        }
    
    def load(self, data:dict):
        self.map_name = data["map_name"]
        self.save_data = simpleJDB.database("assets/level/" + self.map_name)
        self.rooms: list[RoomDict] = []
        for r in self.save_data.getkey("level"):
            self.rooms.append(r)
        self.baked_rooms: list[RenderTexture2D] = []
        for r in self.rooms:
            new_texture: RenderTexture2D = load_render_texture(r["width"], r["height"])
            for t in r["tiles"]:
                tile_texture: Texture2D = load_texture("assets/" + t["texture_name"])
                begin_texture_mode(new_texture)
                draw_texture(tile_texture, t["x"], t["y"], WHITE)
                end_texture_mode()
            self.baked_rooms.append(new_texture)
        print(self.baked_rooms)