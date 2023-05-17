from raypyc import *
from src.GameObject import gameObject
from src.Component import component

class camera(component):
    def __init__(self, gameObject: gameObject):
        """
        Initializes the camera.

        Args:
            self (camera): The camera.
            gameObject (gameObject): The parent gameObject of the camera.

        Returns:
            None
        """
        self.resolution = Vector2(320,180)
        self.gameObject = gameObject
        self.offset = Vector2(0,0)
        self.zoom = 1
        self.lerp = True
        self.cam = Camera2D(self.offset, self.gameObject.position, self.gameObject.rotation, self.zoom)
        
        super().__init__(gameObject)

    def update(self, dt: float):
        """
        Updates the camera.

        Args:
            self (camera): The camera.
            dt (float): The time difference since the last update.

        Returns:
            None
        """
        if self.lerp:
            # Calculate the target position based on the game object's position
            target_x = self.gameObject.position.x-int(self.resolution.x)/2/self.cam.zoom - self.cam.offset.x
            target_y = self.gameObject.position.y-int(self.resolution.y)/2/self.cam.zoom - self.cam.offset.y
            
            # Smoothly move the camera towards the target position
            current_x = self.cam.target.x
            current_y = self.cam.target.y
            
            new_x = current_x + (target_x - current_x) * 3 * dt
            new_y = current_y + (target_y - current_y) * 3 * dt
            
            self.cam.target = Vector2(new_x, new_y)
        else:
            self.cam.target = Vector2(self.gameObject.position.x-int(self.resolution.x)/2, self.gameObject.position.y-int(self.resolution.y)/2)
        return super().update(dt)