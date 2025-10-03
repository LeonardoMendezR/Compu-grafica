### extiende de la clase Window de Pyglet. Se encarga de gestionar la creación de la ventana y sus eventos. Crea el contexto de ModernGL para trabajar con OpenGL. Implementa el método on_draw que limpia y renderiza la escena en cada frame. También implementa on_resize para escalar el contexto al escalar la ventana (y que no se vea lento) y run para ejecutar el loop principal de Pyglet.

import moderngl
import pyglet

class Window(pyglet.window.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, resizable=True)
        self.ctx = moderngl.create_context()
        self.ctx.enable(moderngl.DEPTH_TEST)  # Activar depth test
        self.scene = None

    def set_scene(self, scene):
        self.scene = scene
    
    def on_draw(self):
        self.clear()
        self.ctx.clear(depth=1.0)  # Limpiar el depth buffer
        if self.scene:
            self.scene.render()
    
    def on_resize(self, width, height):
        if self.scene:
            self.scene.on_resize(width, height)
    
    def run(self): # activar el loop de la ventana
        pyglet.app.run()