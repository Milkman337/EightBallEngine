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

from pyray import *
import src.Engine as engine

# ---ADD YOUR CUSTOM SCRIPTS HERE---

# -----------------------------------

init_window(1280, 720, "Game Engine")

main_scene = scene("Main Scene", active=True)

#main_scene.load()
cam_go = gameObject(main_scene, name="Camera")
cam = camera(cam_go)
debugMovement(cam_go, 100)

def update():
    main_scene.update(get_frame_time())

def render():
    main_scene.render()

def render_without_cam():
    pass

engine.run_engine(cam.cam, update, render, render_without_cam)