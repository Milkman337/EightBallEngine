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
from src.ParticleSystem import particleSystem, circleSystem, sparkSystem
from src.RectangleRenderer import rectangleRenderer

from raypyc import *
import src.Engine as engine

window_width = 1280
window_height = 720
game_width = 320
game_height = 180

engine.init("EightBallEngine", Vector2(window_width, window_height), Vector2(game_width, game_height))

main_scene = scene("Main Scene", active=True)

cam_go = gameObject(main_scene, name="Camera")
cam = camera(cam_go)


rectangle = gameObject(main_scene, name="Rect")
rec = rectangleRenderer(rectangle, Vector2(20,20), RED)

particle_test = gameObject(main_scene, Vector2(50, 0), name="Particle")
particleSystem(particle_test,
               (Vector2(-30,-30), Vector2(30,30)),
               30,
               [RED, YELLOW, WHITE],
               1,
               (1,2),
               update_rate=1,
               render_batched=False)

def inputs(key):
    # ---ADD INPUTS HERE---
    pass

circle_particle = gameObject(main_scene, name="Circle", position=Vector2(0,0))
c = circleSystem(circle_particle, final_radius=50, thickness_factor=1.2, speed=100)
c.play()

sparks = gameObject(main_scene, Vector2(-30,0), name="Sparks")
s = sparkSystem(sparks)
s.play()

def update():
    rectangle.rotation += 10 * get_frame_time()
    main_scene.update(get_frame_time())

    if (is_key_pressed(KeyboardKey.KEY_SPACE)):
        s.play()
        c.play()

def render():
    main_scene.render()

def render_without_cam():
    pass

engine.run_engine(cam, inputs, update, render, render_without_cam)
