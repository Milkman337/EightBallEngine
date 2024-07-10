from raypyc import *
from src.Component import component
from src.GameObject import gameObject
from src.Camera import camera

class animator:
    def __init__(self, speed:float, texture:Texture2D, gameObject:gameObject, name:str):
        """
        Initializes the animation

        Args:
            self (animation): Instance of the animation.\n
            speed (float): The speed at wich the animation is played.\n
            texture (Texture2D): The texture of the animation.\n
            gameObject (gameObject): The parent gameObject of the animation(animator).\n

        Returns:
            None
        """
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
        """
        Updates the animation.

        Args:
            self (animation): Instance of the animation.\n
            dt (float): deltaTime.\n

        Returns:
            None
        """
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
        """
        Renders the animation.

        Args:
            self (animation): Instance of the animation.\n

        Returns:
            None
        """
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
        """
        Initializes the animator.

        Args:
            self (animator): The animator.\n
            gameObject (gameObject): The parent gameObject of the animator.\n
            speed (float): Speed of the animations.\n

        Returns:
            None
        """
        super().__init__(gameObject)
        self.speed = speed
        self.selected:str = "None"
        self.animations:list[animaton]=[animaton(self.speed, load_texture("assets/animations/None.png"), self.gameObject, "None")]

    def mirror(self, mirror:bool):
        """
        Mirrors the active animation.

        Args:
            self (animator): The animator.\n
            mirror (bool): This sets if the animation should be mirrored.\n

        Returns:
            None
        """
        for a in self.animations:
            if mirror:
                a.mirror=-1
            else:
                a.mirror=1

    def play(self, animation_name:str):
        """
        Plays a specific animation by name.

        Args:
            self (animator): The animator.\n
            animation_name (str): The name of the animation.\n

        Returns:
            None
        """
        self.selected = animation_name

    def add_animation(self, speed:float, name:str):
        """
        Adds a new animation to the animator.

        Args:
            self (animator): The animator.
            speed (float): Speed of the new animation.
            name (str): The name of the new animation.

        Returns:
            None
        """
        self.animations.append(animaton(speed, load_texture("assets/animations/"+name+".png"), self.gameObject, name))

    def update(self, dt: float):
        """
        Updates the animator.

        Args:
            self (animator): The animator.
            dt (float): The time difference since the last update.

        Returns:
            None
        """
        for a in self.animations:
            if a.name == self.selected:
                a.update(dt)
        return super().update(dt)
    
    def render(self):
        """
        Renders the animator.

        Args:
            self (animator): The animator.

        Returns:
            None
        """
        for a in self.animations:
            if a.name == self.selected:
                a.render()
        return super().render()
    
    
