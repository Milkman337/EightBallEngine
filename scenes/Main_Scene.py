from src.Animator import animator
from src.Camera import camera
from src.Collider import collider
from src.ColliderMap import colliderMap
from src.DebugMovement import debugMovement
from src.DebugRenderer import debugRenderer
from src.GameObject import gameObject
from src.Scene import scene
from src.Script import script
from src.SpriteMap import spriteMap

from pyray import *

class SCENE:
    def __init__(self, s:scene) -> None:
        self.scene:scene = s
        # ---DO EVERYTHING HERE---

        square = gameObject(self.scene, name="Square", position=Vector2(0,0))
        debugRenderer(square)