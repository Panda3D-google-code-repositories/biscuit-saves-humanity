#######################################################
# Space.py - A place for interactions.
# Authors : Justin Sweitzer, Ben Sweitzer
# Started development 04/04/2013
# Version 0.1
#
#######################################################


import direct.directbase.DirectStart
from panda3d.core import WindowProperties
from panda3d.core import Point3,Vec3,Vec4
from direct.showbase.DirectObject import DirectObject

class Space(DirectObject):

    def __init__(self):
#This will use the textured model named "Model" as the boundry and area to move in
#        self.space = loader.loadModel("Model")
#        self.space.reparentTo(render)

        #This uses the mouse to control the camera.
        base.disableMouse()
        props = WindowProperties()
        props.setCursorHidden(True)
        base.win.requestProperties(props)

        self.focus = Vec3(55,-55,20)
        self.heading = 180
        self.pitch = 0
        self.mousex = 0
        self.mousey = 0
        self.last = 0
        self.mousebtn = [0,0,0]

#Currently does nothing other than make a grey window. 
t = Space()

run()

