# EightBallEngine

Discord: https://discord.gg/TN2s7cmfXK

Do you want to create games in python with only code but your projects are getting cluttered. Then you’ve come to the right place. I decided to make my own game engine because I had this exact problem. Also this GameEngine is based on raylib-python-cffi. It’s currently setup for pixel art games with a resolution of 320 by 180. Custom resolutions are in progrss.

## Getting Started

To get started clone this repo and your main file will have a basic starter Project

### Prerequisites

You will need to have raylib installed!

```bash
pip3 install -r "requirements.txt"
```

### Usage

How to do some stuff.

This is the basic [main.py](http://main.py) file.

```python
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

def update():
    rectangle.rotation += 10 * get_frame_time()
    main_scene.update(get_frame_time())

def render():
    main_scene.render()

def render_without_cam():
    pass

engine.run_engine(cam, update, render, render_without_cam)
```

1. You can Organize it even more by creating a scene, running the project once and then it will create a scene script. In there you can just use self.scene instead of main scene.
    
    ```python
    cam_go = gameObject(self.scene, name="Camera")
    ```
    
2. To use the components just import them with from src.[the module] import [Module]
3. Then just add the compoenent to the gameobject:
    
    ```python
    debugMovement(cam_go, 100)
    ```
    
4. To create a custom script for a gameobject import the script component:
    
    ```python
    from src.Script import script
    ```
    
5. Also import your script from assets.scripts
6. A Custom script should look a little something like this:
    
    ```python
    from src.GameObject import gameObject
    from src.Collider import collider
    
    from pyray import *
    
    class yourscriptclass:
        def __init__(self):
            self.gameObject:gameObject = None
    
        def update(self, dt:float):
            pass
    
        def render(self):
            pass
    ```
    
7. The gameobject of the script will automatically be set and is the parent gameobject of the script.
8. And after that just add the script to the gameobject like this:
    
    ```python
    script(gameobject, yourscriptclass())
    ```
    

It’s also very importand to only create the camera in the [main.py](http://main.py) file as it wont work in a scene script.

A huge thanks to Ray for making raylib: https://github.com/raysan5/raylib

And a big thanks also to electronstudio for making raylib-python-cffi: https://github.com/electronstudio/raylib-python-cffi
