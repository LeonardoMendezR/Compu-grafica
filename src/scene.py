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

    def add_object(self, obj, shader_program=None):
        self.objects.append(obj)
        self.graphics[obj.name] = Graphics(self.ctx, shader_program, obj.vertices, obj.indices)

    def render(self):
        self.time += 0.01
        view = self.camera.get_view_matrix()
        projection = self.camera.get_perspective_matrix()
        for obj in self.objects:
            obj.rotation.y += 1  # Rotar el cubo alrededor del eje Y
            obj.rotation.x += math.sin(self.time) * 0.01  # Rotar el cubo alrededor del eje X
            model = obj.get_model_matrix()
            mvp = projection * view * model
            self.graphics[obj.name].set_uniform("Mvp", mvp)
            self.graphics[obj.name].vao.render()
            
    #def render(self):
        #for obj in self.objects:
            # Obtener matrices
            #model = obj.get_model_matrix()
            #view = self.camera.get_view_matrix()
            #projection = self.camera.get_perspective_matrix()
            #mvp = projection * view * model
            # Enviar la matriz MVP al shader
            #self.graphics[obj.name].shader_program.set_uniform("Mvp", mvp)
            # Renderizar el objeto
            #self.graphics[obj.name].vao.render()
    
    def on_resize(self, width, height):
        self.ctx.viewport = (0, 0, width, height)
        self.camera.projection = glm.perspective(glm.radians(45), width / height, 0.1, 100)