from raypyc import *
from src.GameObject import gameObject
from src.Component import component
import random
import copy

class particle:
    def __init__(self,
                 position:Vector2,
                 velocity:Vector2,
                 gravity:float,
                 color:Color,
                 lifetime:float,
                 downscale_factor:float = 1) -> None:
        
        self.position = position
        self.velocity = velocity
        self.gravity = gravity
        self.color = color
        self.lifetime = lifetime
        self.downscale_factor = downscale_factor

    def update(self, dt:float):
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt
        self.lifetime -= self.downscale_factor * dt
        self.velocity.y += self.gravity * dt

    def render(self):
        draw_circle(int(self.position.x), int(self.position.y), self.lifetime*3, self.color)

class sparkSystem(component):
    def __init__(self, gameObject: gameObject,
                 spark_size:float = 0.8,
                 spark_duration:float = 3,
                 spark_length:float = 1,
                 color:Color = WHITE,
                 texture_size:int = 100,
                 amount:int = 6):
        self.spark_size = spark_size
        self.spark_duration = spark_duration
        self.spark_length = spark_length
        self.color = color
        self.amount = amount

        self.time_till_radius = 5
        self.radius = 0

        self.texture = load_render_texture(texture_size, texture_size)

        self.particles:list[particle] = []

        super().__init__(gameObject)

    def play(self):
        begin_texture_mode(self.texture)
        clear_background(Color(0,0,0,0))
        end_texture_mode()
        self.time_till_radius = 5
        self.radius = 0
        for i in range(self.amount):
            self.particles.append(particle(Vector2(self.texture.texture.width/2, self.texture.texture.height/2),
                                           Vector2(random.randrange(-100, 100), random.randrange(-100,100)),
                                           0,
                                           self.color,
                                           self.spark_size,
                                           self.spark_duration))

    def update(self, dt:float):
        self.time_till_radius -= 30 * dt
        if self.time_till_radius <= 0:
            self.radius += self.spark_length*100 * dt
        begin_texture_mode(self.texture)
        for p in self.particles:
            p.update(dt)
            p.render()
        rl_set_blend_factors(0x0302, 0x0302, 0x8007)
        rl_set_blend_mode(BlendMode.BLEND_CUSTOM)
        draw_circle(int(self.texture.texture.width/2), int(self.texture.texture.height/2), self.radius, Color(0,0,0,0))
        rl_set_blend_mode(BlendMode.BLEND_ALPHA)
        end_texture_mode()
        return super().update(dt)
    
    def render(self):
        draw_texture(self.texture.texture, int(self.gameObject.position.x-self.texture.texture.width/2),
                     int(self.gameObject.position.y-self.texture.texture.height/2),
                     WHITE)
        return super().render()

class circleSystem(component):
    def __init__(self, gameObject: gameObject,
                 final_radius:float = 10,
                 thickness_factor:float = 3,
                 color:Color = WHITE,
                 speed:float = 10):
        self.final_radius = final_radius
        self.color = color
        self.speed = speed

        self.thickness_factor = thickness_factor

        self.radius = 0
        self.secondary_radius = 0

        self.running = False

        self.render_texture = load_render_texture(int(final_radius*4+2), int(final_radius*4+2))

        super().__init__(gameObject)

    def play(self):
        self.radius = 0
        self.secondary_radius = 0
        self.running = True

    def update(self, dt:float):
        if self.running:
            self.radius += self.speed * dt
            if (self.radius >= self.final_radius-self.final_radius/self.thickness_factor):
                self.secondary_radius += self.speed * dt * self.final_radius/(self.final_radius/self.thickness_factor)
            if self.radius >= self.final_radius:
                self.running = False
            begin_texture_mode(self.render_texture)
            clear_background(Color(0, 0, 0, 0))
            draw_circle(int(self.render_texture.texture.width/2),
                        int(self.render_texture.texture.height/2),
                        int(self.radius),
                        self.color)
            rl_set_blend_factors(0x0302, 0x0302, 0x8007)
            rl_set_blend_mode(BlendMode.BLEND_CUSTOM)
            draw_circle(int(self.render_texture.texture.width/2),
                        int(self.render_texture.texture.height/2),
                        self.secondary_radius,
                        Color(0,0,0,0))
            rl_set_blend_mode(BlendMode.BLEND_ALPHA)
            end_texture_mode()
        return super().update(dt)
    
    def render(self):
        draw_texture_pro(self.render_texture.texture, 
                         Rectangle(0,0,self.render_texture.texture.width,self.render_texture.texture.height), 
                         Rectangle(self.gameObject.position.x,self.gameObject.position.y,self.render_texture.texture.width,self.render_texture.texture.height), 
                         Vector2(self.render_texture.texture.width/2,self.render_texture.texture.height/2), 
                         0, 
                         WHITE)
        return super().render()

class particleSystem(component):
    def __init__(self, gameObject: gameObject,
                 start_velocity_range:tuple[Vector2, Vector2],
                 gravity:float,
                 colors:list[Color],
                 burst:int,
                 lifetime_range:tuple[float, float] = (1,3),
                 loops:bool = True,
                 update_rate:int = 10,
                 render_batched:bool = True,
                 batched_elements:int = 20):

        self.start_velocity_range = start_velocity_range
        self.gravity = gravity
        self.colors = colors
        self.burst = burst
        self.lifetime_range = lifetime_range
        self.loops = loops
        self.update_rate = update_rate
        self._update_timer = update_rate
        self.render_batched = render_batched

        self.particles:list[particle] = []

        self.batch = rl_load_render_batch(1,batched_elements)

        self.spawn_timer = 1/60*self.update_rate

        self.gameObject:gameObject = gameObject
        super().__init__(gameObject)

    def play(self):
        for i in range(self.burst):
            self.particles.append(particle(Vector2(self.gameObject.position.x, self.gameObject.position.y), Vector2(
                            random.randrange(int(self.start_velocity_range[0].x*100), int(self.start_velocity_range[1].x*100))/100,
                            random.randrange(int(self.start_velocity_range[0].y*100), int(self.start_velocity_range[1].y*100))/100
                        ), self.gravity, random.choice(self.colors), random.randrange(self.lifetime_range[0]*100, self.lifetime_range[1]*100)/100))

    def update(self, dt: float):
        self._update_timer -= 1
        if self._update_timer <= 0:
            
            self._update_timer = self.update_rate
            for p in self.particles:
                p.update(dt=dt*self.update_rate)
                if p.lifetime <= 0:
                    self.particles.remove(p)


        self.spawn_timer -= 1 * dt
        if self.spawn_timer <= 0:
            self.spawn_timer = 1/60*self.update_rate
            # SPAWN PARTICLES
            if self.loops:
                #print("spawned")
                for i in range(self.burst*self.update_rate):
                    self.particles.append(particle(Vector2(self.gameObject.position.x, self.gameObject.position.y), Vector2(
                        random.randrange(int(self.start_velocity_range[0].x*100), int(self.start_velocity_range[1].x*100))/100,
                        random.randrange(int(self.start_velocity_range[0].y*100), int(self.start_velocity_range[1].y*100))/100
                    ), self.gravity, random.choice(self.colors), random.randrange(self.lifetime_range[0]*100, self.lifetime_range[1]*100)/100))

        return super().update(dt)
    
    def render(self):
        if self.render_batched:
            rl_set_render_batch_active(self.batch)
        for p in reversed(self.particles):
            p.render()
        if self.render_batched:
            rl_draw_render_batch_active()
            rl_set_render_batch_active(None)

        return super().render()