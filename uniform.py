from OpenGL.GL import *

class Uniform(object):

    def __init__(self, dataType, data):
        self.dataType = dataType
        # data to be sent to uniform variable
        self.data = data
        # reference for variable location in program
        self.variableRef = None
        # get and store reference for program variablewith given name
    def locateVariable(self, programRef,variableName):
        self.variableRef = glGetUniformLocation(programRef, variableName)
    def uploadData(self):
        if self.variableRef == -1:
            return

        if self.dataType == "int":
            glUniform1i(self.variableRef, self.data)
        elif self.dataType == "bool":
            glUniform1i(self.variableRef, self.data)
        elif self.dataType == "float":
            glUniform1f(self.variableRef, self.data)
        elif self.dataType == "vec2":
            glUniform2f(self.variableRef, self.data[0], self.data[1])
        elif self.dataType == "vec3":
            glUniform3f(self.variableRef, self.data[0], self.data[1],self.data[2])
        elif self.dataType == "vec4":
            glUniform4f(self.variableRef, self.data[0], self.data[1],self.data[2], self.data[3])
