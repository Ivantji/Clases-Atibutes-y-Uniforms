from core.base import Base
from core.openGLUtils import OpenGLUtils
from core.attribute import Attribute
from OpenGL.GL import *


class Test(Base):
    #el método define un código de sombreado de vértices (vsCode) y un código de sombreado de fragmentos (fsCode) como cadenas de varias líneas.
    # El sombreador de vértices toma un solo atributo de entrada, posición, y establece la salida gl_Position en un vector de cuatro componentes que
    # consiste en la posición de entrada.
    def initialize(self):
        print("Initializing program...")
        ### initialize program ###
        vsCode = """
        in vec3 position;
        void main()
        {
            gl_Position = vec4(position.x, position.y, position.z, 1.0);
        }
        """
        fsCode = """ out vec4 fragColor;
        void main()
        {
            fragColor = vec4(1.0, 1.0, 0.0, 1.0);
        }
        """
        #configura un contexto de representación con un código de sombreado de vértices específico (vsCode) y un código de sombreado de fragmentos (fsCode).
        # Inicializa un programa de sombreado con estos códigos y almacena una referencia a él en la variable programRef.
        #el código almacena el número de vértices en la variable vertexCount, que se usará más adelante para especificar cuántos vértices representar.
        self.programRef = OpenGLUtils.initializeProgram(vsCode, fsCode)
        ### render settings (optional) ###
        glLineWidth(4)
        ### set up vertex array object ###
        vaoRef = glGenVertexArrays(1)
        glBindVertexArray(vaoRef)
        ### set up vertex attribute ###
        positionData = [[-0.8, 0.0, 0.0], [0.4, 0.6,0.0],[-0.4, 0.6, 0.0], [0.8, 0.0,0.0],[-0.4, -0.6, 0.0], [0.4,-0.6, 0.0]]
        self.vertexCount = len(positionData)
        positionAttribute = Attribute("vec3",positionData)
        positionAttribute.associateVariable(self.programRef, "position")

#glUseProgram se usa para vincular un programa de sombreado específico (al que hace referencia self.programRef)
    # para usarlo durante el renderizado. Esto especifica el código de sombreado que se usará para procesar
    # los datos de vértices y fragmentos durante el proceso de representación.
    def update(self):
        glUseProgram(self.programRef)
        glDrawArrays(GL_LINE_LOOP, 0, self.vertexCount)
Test().run()