from pyray import *
from typing import Callable

def run_engine(cam:Camera2D, update: callable[[], None], render: callable[[], None], render_without_cam:callable[[], None]=None):
    """
    Starts the GameEngine.

    Args:
        cam (Camera2D): The camera you want to render with.\n
        update (callable[[], None]): gets called every frame and is used for logic.\n
        render (callable[[], None]): gets called once every frame and is used for rendering.\n
        render_without_cam (callable[[], None]): same as render but is not rendered with the camera. This can be used for GUI.\n
    
    Return:
        None
    """
    screen = load_render_texture(320, 180)
    while not window_should_close():
        update()

        begin_drawing()
        clear_background(BLACK)
        begin_texture_mode(screen)
        clear_background(BLACK)
        begin_mode_2d(cam)

        render()

        end_mode_2d()
        end_texture_mode()

        draw_texture_pro(screen.texture,
                        Rectangle(0,0,320,-180),
                        Rectangle(0,0,1280,720),
                        Vector2(0,0),
                        0,
                        WHITE)
        
        render_without_cam()
        
        draw_fps(0,0)
        end_drawing()