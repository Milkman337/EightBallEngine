from pyray import *
from src.Component import component
from src.GameObject import gameObject
from src.Camera import camera

class animaton:
    def __init__(self, speed:float, texture:Texture2D, gameObject:gameObject, name:str):
        self.name = name
        self.gameObject = gameObject
        self.speed = speed
        self.texture = texture
        self.frame_rec = Rectangle(0,0,self.texture.height, self.texture.height)
        self.frame = 0
        self.frames = self.texture.width/self.texture.height
        self.frame_timer = 1
        self.between = load_render_texture(int(self.frame_rec.width), int(self.frame_rec.height))
        self.mirror = 1
        

    def update(self, dt: float):
        begin_texture_mode(self.between)
        clear_background(Color(0,0,0,0))
        draw_texture_rec(self.texture, self.frame_rec, Vector2(0,0), WHITE)
        end_texture_mode()
        self.frame_timer-=self.speed*dt
        if self.frame_timer<=0:
            self.frame_timer = 1
            self.frame+=1
            if self.frame>=self.frames:
                self.frame=0
            self.frame_rec.x=self.texture.height*self.frame

    def render(self):
                
        draw_texture_pro(self.between.texture,
                         Rectangle(0,0,self.between.texture.width*self.mirror, -self.between.texture.height),
                         Rectangle(self.gameObject.position.x,
                                   self.gameObject.position.y,
                                   self.between.texture.width*self.gameObject.scale.x,
                                   self.between.texture.height*self.gameObject.scale.y),
                                   Vector2(self.between.texture.width*self.gameObject.scale.x/2, self.between.texture.height*self.gameObject.scale.y/2),
                                   self.gameObject.rotation,
                                   WHITE)

class animator(component):
    def __init__(self, gameObject: gameObject,
                 speed:float=8):
        super().__init__(gameObject)
        self.speed = speed
        self.selected:str = "None"
        self.animations:list[animaton]=[animaton(self.speed, load_texture("assets/animations/None.png"), self.gameObject, "None")]

    def mirror(self, mirror:bool):
        for a in self.animations:
            if mirror:
                a.mirror=-1
            else:
                a.mirror=1

    def play(self, animation_name:str):
        self.selected = animation_name

    def add_animation(self, speed:float, name:str):
        self.animations.append(animaton(speed, load_texture("assets/animations/"+name+".png"), self.gameObject, name))

    def update(self, dt: float):
        for a in self.animations:
            if a.name == self.selected:
                a.update(dt)
        return super().update(dt)
    
    def render(self):
        for a in self.animations:
            if a.name == self.selected:
                a.render()
        return super().render()
    
    