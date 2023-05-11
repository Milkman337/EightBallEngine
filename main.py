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

# --ADD YOU CUSTOM SCRIPTS HERE--

# -------------------------------

init_window(1280, 720, "Game Engine")

main_scene = scene("Main Scene", active=True)

#main_scene.load()
cam_go = gameObject(main_scene, name="Camera")
cam = camera(cam_go)
debugMovement(cam_go, 100)

screen = load_render_texture(320, 180)
while not window_should_close():
    main_scene.update(get_frame_time())

    begin_drawing()
    clear_background(BLACK)
    begin_texture_mode(screen)
    clear_background(BLACK)
    begin_mode_2d(cam.cam)

    main_scene.render()

    end_mode_2d()
    end_texture_mode()

    draw_texture_pro(screen.texture,
                     Rectangle(0,0,320,-180),
                     Rectangle(0,0,1280,720),
                     Vector2(0,0),
                     0,
                     WHITE)
    

    
    draw_fps(0,0)
    end_drawing()

#main_scene.save()