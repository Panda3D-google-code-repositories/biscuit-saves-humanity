#!/usr/bin/env python

#######################################################
# main.py - main game portion
# Authors : Justin Sweitzer, Ben Sweitzer
# Started development 04/04/2013
# Version 0.1a
#
#######################################################


"""This is the main portion of the code. I think that what I want is for this file to handle generation of the gamespace and 
tracking of the player location, as well as ship configuration, etc. Graphics can be overlayed on top of this using Panda3D or
even pygame (to start). That way we can wrap whatever graphics we want around a complete game. """

import random
import time

class Planet():
    """Planet represents a single planet member of a solar system."""
    def __init__(self):
        
        self.Uranium=0
        self.Titanium=0
        self.Hydrocarbons=0
        self.Water=0
        self.Silicon=0
        self.Size=1
        
    def SetPlanetSize(self,PlanetSize):
        self.Size=PlanetSize
        
    def SetResource(self,resource):
        if resource == 'Hydrocarbons':
            self.Hydrocarbons = (random.randint(1,10))
        elif resource == 'Titanium':
            self.Titanium = (random.randint(1,10))
        elif resource == 'Uranium':
            self.Uranium = (random.randint(1,10))            
        elif resource == 'Water':
            self.Water = (random.randint(1,10))
        elif resource == 'Silicon':
            self.Silicon = (random.randint(1,10))
        else:
            pass
        
class Star():
    """Star is a class to represent a solar system. It will comprise one star and a random number of instances of 'Planet'"""
    def __init__(self,name,bbox):
        self.NumPlanets = random.randint(1,12)
        self.PlanetList = [Planet() for i in range(0,self.NumPlanets)]
        # Set Planet() atts by starname.PlanetList[i].method() ...
        self.name = name
        self.StarType = random.randint(1,4)
        self.Coordinates = (random.randint(bbox[0][0],bbox[1][0]),random.randint(bbox[0][0],bbox[1][0]),random.randint(bbox[0][0],bbox[1][0]))
       
        
    def __getitem__(self,i):
        # getitem to return a specific 'planet' instance
        # I think this will let you set Planet() atts by starname[i].planetmethod()
        return(self.PlanetList[i])
        
    def GetNumPlanets(self):
        # return the number of planets associated with this star
        return(len(self.PlanetList))
        
    def GetSystemName(self):
        return(self.name)
    
    def SetNumberofPlanets(self,NumPlanets):
        # in case there's any reason to change these...
        self.NumPlanets = NumPlanets
        self.PlanetList = []
        self.PlanetList = [ Planet() for i in range(0,self.NumPlanets)]
    
    def SetStarType(self,StarType):
        # Maybe use this to set red/white dwarf, main sequence, etc...
        # Or just leave them all the same...
        pass
    
    
class GalaxyChunk():
    
    """GalaxyChunk is a section of space explorable by the player. It is not representative of any part of the Milky Way,
    because it's a lot easier to generate a random collection of stars than it would be to put them all in the right places.""" 
    
    def __init__(self):
        bbox = ((-100000,-100000,-100000),(100000,100000,100000))       # The galaxy chunk is bounded by a 100,000 light year cube
        self.Earth = (0,0,0)                                            # Earth, of course, is the reference point within the cube.
        self.numStars = 150                                                  # Number of stars to fill the void with
        
        self.StarList = [ Star('test',bbox) for i in range(0,self.numStars) ]
        
    def SeedStarList(self,numStars):
        """ This method should seed the star list with planets and resources. I am giving each star between 1 and 12 planets.
        Because of the way I am wanting to do this (simple), it is possible that more 'resource planets' can be assigned to a 
        system than the number of planets in that system.  To counter that, I want to just assign multiple resources to individual
        planets. """
        
        InhabitablePlanets = []
        UraniumPlanets = []
        WaterPlanets = []
        TitaniumPlanets = []
        HydrocarbonPlanets = []
        SiliconPlanets = []
        
        numInhabitablePlanets = numStars / 30
        numUraniumPlanets = numStars / 4
        numTitaniumPlanets = numStars / 2
        numWaterPlanets = numStars
        numHydrocarbonPlanets = numStars / 2
        numSiliconPlanets = numStars


                
            
        
        
        

                                                                
            
        
        
        
