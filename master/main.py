#!/usr/bin/env ppython
#######################################################
# main.py - Handles creation of all objects and game logic
# Authors : Justin Sweitzer, Ben Sweitzer
# Started development 04/04/2013
# Version 0.1
#
#######################################################


import sys, os
from direct.showbase.ShowBase import ShowBase
from panda3d.core import *


root = './'

sys.path.append(os.path.join(root,'rendering'))
sys.path.append(os.path.join(root,'bases'))
sys.path.append(os.path.join(root,'aliens'))
sys.path.append(os.path.join(root,'ships'))
sys.path.append(os.path.join(root,'galaxy'))

import random, aliens, galaxy, starbase, ships, components

g=galaxy.GalaxyChunk(root)

alienList=[]
for file in os.listdir(os.path.join(root,'aliens')):
    if '.alien' in file:
        alienList.append(aliens.Alien(g.StarList,os.path.join(root,'aliens',file)))
ship = ships.CapitalShip('Explorer',root)
       


class BiscuitRun(ShowBase):
    
    def __init__(self):
        ShowBase.__init__(self)
        
        # Make a chase camera for the ship
        chaser = self.render.attachNewNode("chaser")
        chaser.setPos(ship.Coordinates)
        chaser.setHpr(0,0,0)
        base.camera.reparentTo(chaser)
        
        # Make the background the black of space
        self.setBackgroundColor(0,0,0,1) 
        
        # Create Ambient Light (white, why not?)
        ambientLight = AmbientLight('ambientLight')
        ambientLight.setColor(Vec4(0.1, 0.1, 0.1, 1))
        ambientLightNP = render.attachNewNode(ambientLight)
        render.setLight(ambientLightNP)
        # This is an alternative color:
        ambient = AmbientLight('ambient')
        ambient.setColor(Vec4(255, 50, 0, 0.5))
        
        scalefactor = 1.e-1
        # Loads all of the stars at once... 
        for i in range(0,150):
           
           self.environ = self.loader.loadModel(g[i].Model)
           # Reparent model to render ... wtf ever that means
           self.environ.reparentTo(self.render)
           # Scale and position transforms ... sure we'll need these at some point
           self.environ.setScale(g[i].Size*scalefactor,g[i].Size*scalefactor,g[i].Size*scalefactor)
           self.environ.setPos(g[i].Coordinates)
           environNP = self.environ.attachNewNode(ambient)
           self.environ.setLight(environNP)
        
        self.sol = self.loader.loadModel(g.Sol.Model)
        self.sol.reparentTo(self.render)
        self.sol.setScale(g.Sol.Size*scalefactor,g.Sol.Size*scalefactor,g.Sol.Size*scalefactor)
        self.sol.setPos(g.Sol.Coordinates)
        solNP = self.sol.attachNewNode(ambient)
        self.sol.setLight(solNP)
                
        self.ship = self.loader.loadModel(ship.Model) 
        self.ship.setScale(1e-2,1e-2,1e-2)
        self.ship.setPos(ship.Coordinates)       
        shipNP = self.ship.attachNewNode(ambient)
        self.ship.setLight(shipNP)
        self.ship.reparentTo(chaser)
        
        speed = 1
        vel = self.render.getRelativeVector(chaser,Vec3(0,speed,0))
        def chase_task(task):
            dt = globalClock.getDt()
            chaser.setPos(chaser.getPos()+vel*dt)
            return(task.cont)
        task = taskMgr.add(chase_task,"chase-task")

        
        
BiscuitSavesHumanity = BiscuitRun()
BiscuitSavesHumanity.run()

        