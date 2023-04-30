from core.base import Base
from core.openGLUtils import OpenGLUtils
from core.attribute import Attribute
from OpenGL.GL import *
class Test(Base):
    def initialize(self):
        print("Initializing program...")
        #efine la posición de los atributos de vértice y vertexColor, y el color de la variable de salida, que se pasará
        # al sombreador de fragmentos. En la función main(), establece la variable integrada gl_Position en un vector de
        # 4 componentes con la posición del vértice en coordenadas homogéneas (x, y, z, 1.0) y establece la variable de
        # color en el atributo de entrada vertexColor.
        vsCode = """
        in vec3 position;
        in vec3 vertexColor;
        out vec3 color;
        void main()
        {
            gl_Position = vec4(position.x, position.y,position.z, 1.0);
            color = vertexColor;
        }
        """
        #La variable de entrada de color vec3 es el color calculado en el vertex shader para cada vértice del objeto
        # renderizado, y fragColor es la variable de salida que especifica el color final del fragmento.
        fsCode = """
        in vec3 color;
        out vec4 fragColor;
        void main()
        {
           fragColor = vec4(color.r, color.g,color.b, 1.0);
        }
        """
        #glGenVertexArrays genera uno o más nombres de objeto de matriz de vértices y los devuelve como valores enteros sin signo.
        self.programRef = OpenGLUtils.initializeProgram(vsCode, fsCode)
        glPointSize(10)
        glLineWidth(4)
        vaoRef = glGenVertexArrays(1)
        glBindVertexArray(vaoRef)
### set up vertex attributes ###
        #inicializa dos atributos, positionAttribute y colorAttribute, y los asocia con las variables de sombreado
        # de vértices position y vertexColor, respectivamente. positionData y colorData son matrices que contienen los
        # valores de posición y color de cada vértice del hexágono.
        positionData = [[0.8, 0.0, 0.0], [0.4, 0.6,0.0],[-0.4, 0.6, 0.0], [-0.8, 0.0, 0.0], [-0.4,-0.6, 0.0], [0.4, -0.6, 0.0]]
        self.vertexCount = len(positionData)
        positionAttribute = Attribute("vec3",positionData)
        positionAttribute.associateVariable(
        self.programRef, "position")
        colorData = [[1.0, 0.0, 0.0], [1.0, 0.5,0.0],[1.0, 1.0, 0.0], [0.0, 1.0, 0.0], [0.0,0.0, 1.0], [0.5, 0.0, 1.0]]
        colorAttribute = Attribute("vec3", colorData)
        colorAttribute.associateVariable(self.programRef, "vertexColor")
#actualizando la ventana gráfica, borrando el búfer de color y llamando a la función glDrawArrays para representar la geometría.
    def update(self):
        glUseProgram(self.programRef)
        glDrawArrays( GL_TRIANGLE_FAN, 0, self.vertexCount)
Test().run()

