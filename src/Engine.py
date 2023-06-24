from raypyc import *
from typing import Callable
from src.Camera import camera
from src.GlobalVars import keys

_game_name = None
_resolution = None
_game_resolution = None

def init(game_name: str, resolution:Vector2, game_resolution:Vector2):
    global _game_name, _resolution, _game_resolution
    _game_name = game_name
    _resolution = resolution
    _game_resolution = game_resolution

    init_window(int(resolution.x), int(resolution.y), game_name.encode())
    init_audio_device()

def get_pressed_key():
    for key in keys:
        if is_key_down(key):
            return keys[key]

    for key in keys:
        if is_key_released(key):
            return str(keys[key] + " up")

def run_engine(cam:camera, inputs, update, render, render_without_cam=None):
    """
    Starts the GameEngine.

    Args:
        cam (camera): The camera you want to render with.\n
        inputs (function): gets called every frame and is takes care of detecting keyboard and mouse inputs.\n
        update (function): gets called every frame and is used for logic.\n
        render (function): gets called once every frame and is used for rendering.\n
        render_without_cam (function): same as render but is not rendered with the camera. This can be used for GUI.\n
    
    Return:
        None
    """

    cam.resolution = _game_resolution

    screen = load_render_texture(int(_game_resolution.x), int(_game_resolution.y))
    while not window_should_close():
        update()

        key_pressed = get_pressed_key()
        if key_pressed is not None:
            inputs(key_pressed)

        begin_drawing()
        clear_background(BLACK)
        begin_texture_mode(screen)
        clear_background(BLACK)
        begin_mode_2d(cam.cam)

        render()

        end_mode_2d()
        end_texture_mode()

        draw_texture_pro(screen.texture,
                        Rectangle(0,0,int(_game_resolution.x),-int(_game_resolution.y)),
                        Rectangle(0,0,int(_resolution.x),int(_resolution.y)),
                        Vector2(0,0),
                        0,
                        WHITE)
        
        render_without_cam()
        
        draw_fps(0,0)
        end_drawing()