### ejecuta el programa. Crea una ventana Window, un ShaderProgram, una Scene, crea las instancias de los objetos gráficos (en este caso Cube), crea la cámara y la posiciona. Por último, agrega los objetos en la escena y corre el loop principal del programa.

from window import Window
from shader_program import ShaderProgram
from cube import Cube
from camera import Camera
from scene import Scene

# Ventana
window = Window(800, 600, "Basic Graphic Engine")
# Shader
shader_program = ShaderProgram(window.ctx, '../shaders/basic.vert', '../shaders/basic.frag')

# Camara
camera = Camera((0, 0, 6), (0, 0, 0), (0, 1, 0), 100, window.width / window.height, 0.1, 100.0)

# Objetos
cube1 = Cube((-2, 0, 0), (0, 45, 0), (1, 1, 1), name="Cube1")
cube2 = Cube((2, 0, 0), (0, 45, 0), (1, .5, 1), name="Cube2")

# Escena
scene = Scene(window.ctx, camera)
scene.add_object(cube1, shader_program)
scene.add_object(cube2, shader_program)

# Carga de la escena y ejecucuin del loop principal
window.set_scene(scene)
window.run()
