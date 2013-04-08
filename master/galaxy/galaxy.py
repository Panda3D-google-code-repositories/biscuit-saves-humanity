 
#!/usr/bin/env python

#######################################################
# galaxy.py - Generates the known chunk of galaxy.
# Authors : Justin Sweitzer, Ben Sweitzer
# Started development 04/04/2013
# Version 0.1
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
        self.Inhabitable=0
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
        elif resource == 'Inhabitable':
            self.Inhabitable = 1
       
        else:
            pass
       
    def GetResourceList(self):
        return(('Uranium',self.Uranium,'Titanium',self.Titanium,'Water',self.Water,'Hydrocarbons',self.Hydrocarbons,'Silicon',self.Silicon,'Inhabitable', self.Inhabitable))
       
class Star():
    """Star is a class to represent a solar system. It will comprise one star and a random number of instances of 'Planet'"""
    def __init__(self,name,bbox):
        self.NumPlanets = random.randint(1,12)
        self.PlanetList = [Planet() for i in range(0,self.NumPlanets)]
        # Set Planet() atts by starname.PlanetList[i].method() ...
        self.name = name
        self.StarType = random.randint(1,4)
        self.Coordinates = (random.randint(bbox[0][0],bbox[1][0]),random.randint(bbox[0][0],bbox[1][0]),random.randint(bbox[0][0],bbox[1][0]))
        self.IsAlienSystem = 0
        self.Explored = 0
       
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
    
    def StoreDistances(self,StarList):
        j=0
        self.DistanceList = []
        for star in StarList:
            self.DistanceList.append([(sum((star.Coordinates[i] - self.Coordinates[i])**2 for i in range(0,3)))**0.5,j,star])
            self.DistanceList = sorted(self.DistanceList)
            j+=1
            
    def GetDistances(self):
        return(self.DistanceList)
        
    def SetInhabitants(self,name,basetype):
        self.IsAlienSystem = 1
        self.InhabitantName = name
        self.BaseType = basetype
        
    def Probe(self):
        i=0
        resinfo = []
        for planet in self.PlanetList:
            resinfo.append(['%s %i' % (self.name, i), planet.GetResourceList()])
            i+=1
            
        if self.IsAlienSystem == 0:
            return(resinfo)
        else:
            return('%s %s') % (self.InhabitantName, self.BaseType)
                
class GalaxyChunk():
   
    """GalaxyChunk is a section of space explorable by the player. It is not representative of any part of the Milky Way,
    because it's a lot easier to generate a random collection of stars than it would be to put them all in the right places."""
   
    def __init__(self):
        bbox = ((-5000,-5000,-5000),(5000,5000,5000))       # The galaxy chunk is bounded by a 10,000 light year cube
        self.Earth = (0,0,0)                                            # Earth, of course, is the reference point within the cube.
        self.numStars = 150                                             # Number of stars to fill the void with
       
        self.StarList = [ Star('test',bbox) for i in range(0,self.numStars) ]
        self.TotalNumPlanets = sum(self.StarList[i].GetNumPlanets() for i in range(0,self.numStars))
        self.SeedStarList()
   
    def __getitem__(self,i):
        return(self.StarList[i])                                         # hoping this means I can call a planet by galaxy[i][j]
       
    def SeedStarList(self):
        """ This method seeds the planet instances with resources"""
       
        resdict = {1: 'Inhabitable', 2: 'Uranium', 3: 'Water', 4: 'Titanium', 5: 'Hydrocarbons', 6: 'Silicon'}
       
        InhabitablePlanets = []
        UraniumPlanets = []
        WaterPlanets = []
        TitaniumPlanets = []
        HydrocarbonPlanets = []
        SiliconPlanets = []
       
        numInhabitablePlanets = self.numStars / 30
        numUraniumPlanets = self.numStars / 4
        numTitaniumPlanets = self.numStars / 2
        numWaterPlanets = self.numStars
        numHydrocarbonPlanets = self.numStars / 2
        numSiliconPlanets = self.numStars
       
        samp_range = set((1,2,3,4,5))
       
        for i in range(0,self.numStars):
            self[i].StoreDistances(self.StarList)
            for j in range(0,self[i].GetNumPlanets()):
               
                if numInhabitablePlanets+numWaterPlanets+numHydrocarbonPlanets+numTitaniumPlanets+numUraniumPlanets+numSiliconPlanets == 0:
                    break
                if numInhabitablePlanets == 0:
                    samp_range -= set((1,0))
                if numUraniumPlanets == 0:
                    samp_range -= set((2,0))
                if numWaterPlanets == 0:
                    samp_range -= set((3,0))
                if numTitaniumPlanets == 0:
                    samp_range -= set((4,0))
                if numSiliconPlanets == 0:
                    samp_range -= set((5,0))
                luckynum = random.sample(samp_range,1)[0]
                self[i][j].SetResource(resdict[luckynum])



                   
 
           

