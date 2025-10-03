### posiciona una cámara, administra los objetos y sus Graphics (VBO, VAO, ShaderProgram). Realiza transformaciones a los objetos que están en la escena y actualiza sus shaders. También actualiza viewport en on_resize.

import math
from graphics import Graphics
import glm

class Scene:
    def __init__(self, ctx, camera):
        self.ctx = ctx
        self.objects = []
        self.graphics = {}
        self.camera = camera
        self.model = glm.mat4(1)
        self.time = 0.0  # Inicializar self.time
        self.time += 0.01
        self.view = self.camera.get_view_matrix()
        self.projection = self.camera.get_perspective_matrix()

    def add_object(self, obj, shader_program=None):
        self.objects.append(obj)
        self.graphics[obj.name] = Graphics(self.ctx, shader_program, obj.vertices, obj.indices)

    def render(self):
        self.time += 0.01
        
        for obj in self.objects:
            obj.rotation.y += 1.0  # Rotar el objeto en el eje Y
            obj.rotation.x += 0.5  # Rotar el objeto en el eje X
            obj.rotation.z += 0.2  # Rotar el objeto en el eje Z
            
            obj.position.x += math.sin(self.time) * 0.01
            model = obj.get_model_matrix()
            mvp = self.projection * self.view * model
            self.graphics[obj.name].set_uniform("Mvp", mvp)
            self.graphics[obj.name].vao.render()

    def on_mouse_click(self, u, v):
        ray = self.camera.raycast(u, v)
        
        for obj in self.objects:
            if obj.check_hit(ray.origin, ray.direction):
                if obj.name == "Cube1":
                    print(f"Le re atinaste al cubito del brian wachin!")
                else:
                    print(f"Wachin le pegaste al cubo del juan rescatate ñeri!")
    
    def on_resize(self, width, height):
        self.ctx.viewport = (0, 0, width, height)
        self.camera.projection = glm.perspective(glm.radians(45), width / height, 0.1, 100)