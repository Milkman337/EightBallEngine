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
from src.RectangleRenderer import rectangleRenderer

from pyray import *
import src.Engine as engine

window_width = 720
window_height = 520
game_width = 320
game_height = 180

engine.init("EightBallEngine", Vector2(window_width, window_height), Vector2(game_width, game_height))

main_scene = scene("Main Scene", active=True)

cam_go = gameObject(main_scene, name="Camera")
cam = camera(cam_go)


rectangle = gameObject(main_scene, name="Rect")
rec = rectangleRenderer(rectangle, scale=Vector2(20,20), Color=YELLOW)

def inputs(key):
    if (key == "W"):
        rectangle.position.y -= 200 * get_frame_time()

    if (key == "S"):
        rectangle.position.y += 200 * get_frame_time()

    if (key == "A"):
        rectangle.position.x -= 200 * get_frame_time()

    if (key == "D"):
        rectangle.position.x += 200 * get_frame_time()



def update():
    main_scene.update(get_frame_time())
    rectangle.rotation += 50 * get_frame_time()

def render():
    main_scene.render()


def render_without_cam():
    pass

engine.run_engine(cam.cam, inputs, update, render, render_without_cam)
