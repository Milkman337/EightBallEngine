from src.Component import component
from src.GameObject import gameObject
from src.Scene import scene
from src.DebugRenderer import debugRenderer
from src.DebugMovement import debugMovement
from src.SpriteRenderer import spriteRenderer
from src.SpriteMap import spriteMap
from src.Collider import collider
from src.Animator import animator
from src.Script import script
from src.Camera import camera
from src.RectangleRenderer import *

from pyray import *
import src.Engine as engine

window_width = 1280
window_height = 720

init_window(window_width, window_height, "Game Engine")
main_scene = scene("Main Scene", active=True)

cam_go = gameObject(main_scene, name="Camera")
cam = camera(cam_go)


rectangle = gameObject(main_scene, name="Rect")
rec = RectangleObject(rectangle, position=Vector2(10, 10), scale=Vector2(20,20), active=True, tint=YELLOW)

def update():
    main_scene.update(get_frame_time())

def render():
    main_scene.render()

def render_without_cam():
    pass

engine.run_engine(cam.cam, update, render, render_without_cam)
