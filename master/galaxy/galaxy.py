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
import time, os



class Planet():
    """Planet represents a single planet member of a solar system."""
    def __init__(self,root):
       
        self.Uranium=0
        self.Titanium=0
        self.Hydrocarbons=0
        self.Water=0
        self.Silicon=0
        self.Inhabitable=0
        self.Size=random.randint(1,1000) # Call 2 the size of earth ... over 100 -> gas giant
        self.Dilithium=0
        self.Model = os.path.join(root,'models/planets/planet.egg')
       
    def SetPlanetSize(self,PlanetSize):
        self.Size=PlanetSize
       
    def SetResource(self,resource):
        
        if self.Size >= 100:
            self.Type = 'Gas Giant'
        if self.Size <= 10 and random.randint(1,10) <= 7:
            self.Inhabitable = 1
            self.Type = 'Class M'
            return(1)
       
        if resource == 'Hydrocarbons':
            self.Hydrocarbons = (random.randint(50,200))
        elif resource == 'Titanium':
            self.Titanium = (random.randint(10,50))
        elif resource == 'Uranium':
            self.Uranium = (random.randint(1,10))            
        elif resource == 'Water':
            self.Water = (random.randint(100,1000))
        elif resource == 'Silicon':
            self.Silicon = (random.randint(10,150))
        elif resource == 'Inhabitable':
            self.Inhabitable = 1
        elif resource == 'Dilithium':
            self.Dilithium = (random.randint(1,10))
       
        else:
            pass
        return(0)
       
    def GetResourceList(self):
        return([['Uranium',self.Uranium],['Titanium',self.Titanium],['Water',self.Water],['Hydrocarbons',self.Hydrocarbons],['Silicon',self.Silicon],['Dilithium',self.Dilithium],['Inhabitable', self.Inhabitable]])
       
class Star():
    """Star is a class to represent a solar system. It will comprise one star and a random number of instances of 'Planet'"""
    def __init__(self,name,pvtname,bbox,root):
        self.NumPlanets = random.randint(1,12)
        self.PlanetList = [Planet(root) for i in range(0,self.NumPlanets)]
        # Set Planet() atts by starname.PlanetList[i].method() ...
        self.Name = name
        self.Model = os.path.join(root,'galaxy/models/stars/star.egg')
        self.pvtname = pvtname
        self.StarType = random.randint(1,4)
        self.Coordinates = (random.randint(bbox[0][0],bbox[1][0]),random.randint(bbox[0][0],bbox[1][0]),random.randint(bbox[0][0],bbox[1][0]))
        self.IsAlienSystem = 0
        self.Explored = 0
        self.Size = random.randint(1,100) #*(1.47031956e-7/25.0)  # 25 = size of sun, why not?
                                                                # 1.470315956e-7 = diameter of sun in ly
                                                                
       
    def __getitem__(self,i):
        # getitem to return a specific 'planet' instance
        # I think this will let you set Planet() atts by starname[i].planetmethod()
        return(self.PlanetList[i])
       
    def GetNumPlanets(self):
        # return the number of planets associated with this star
        return(len(self.PlanetList))
       
    def GetSystemName(self):
        return(self.Name+' System')
   
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
        self.Name = self.pvtname
        i=0
        resinfo = []
        for planet in self.PlanetList:
            resinfo.append(['%s %i' % (self.Name, i), planet.GetResourceList()])
            i+=1
           
        if self.IsAlienSystem == 0:
            return(resinfo)
        else:
            self.Name ='%s %s' % (self.InhabitantName, self.BaseType)
            return(self.Name)
            
    def Harvest(self):
        Uranium=Titanium=Water=Hydrocarbons=Silicon=Dilithium=Inhabitable = 0
        
        for planet in self.PlanetList:
            
            Uranium+= planet.Uranium
            Titanium+= planet.Titanium
            Water+= planet.Water
            Hydrocarbons+= planet.Hydrocarbons
            Silicon+= planet.Silicon
            Dilithium+= planet.Dilithium
            Inhabitable+= planet.Inhabitable
            planet.Uranium=planet.Titanium=planet.Water=planet.Hydrocarbons=planet.Silicon=planet.Dilithium=planet.Inhabitable = 0
            
        return(Uranium,Titanium,Water,Hydrocarbons,Silicon,Dilithium,Inhabitable)
               
class GalaxyChunk():
   
    """GalaxyChunk is a section of space explorable by the player. It is not representative of any part of the Milky Way,
    because it's a lot easier to generate a random collection of stars than it would be to put them all in the right places."""
   
    def __init__(self,root):
        bbox = ((-5000,-5000,-5000),(5000,5000,5000))       # The galaxy chunk is bounded by a 10,000 light year cube
        self.Sol = Star('Sol','Sol',((0,0,0),(0,0,0)),root)                      # Earth, of course, is the reference point within the cube.
        self.Sol.NumPlanets = 9
        self.Sol.Size = 25 #1.47031956e-7
        self.numStars = 150                                             # Number of stars to fill the void with
        f1 = open(os.path.join(root,'galaxy/StarNames.stars'),'r')
        starNames = f1.readlines()
        f1.close()
        random.shuffle(starNames)
        self.StarList = [ Star('Unknown System',starNames[i].strip(),bbox,root) for i in range(0,self.numStars) ]
        self.TotalNumPlanets = sum(self.StarList[i].GetNumPlanets() for i in range(0,self.numStars))
        self.SeedStarList()
   
    def __getitem__(self,i):
        return(self.StarList[i])                                         # hoping this means I can call a planet by galaxy[i][j]
       
    def SeedStarList(self):
        """ This method seeds the planet instances with resources"""
       
        resdict = {1: 'Inhabitable', 2: 'Uranium', 3: 'Water', 4: 'Titanium', 5: 'Hydrocarbons', 6: 'Silicon', 7:'Dilithium'}
       
        InhabitablePlanets = []
        UraniumPlanets = []
        WaterPlanets = []
        TitaniumPlanets = []
        HydrocarbonPlanets = []
        SiliconPlanets = []
       
        numInhabitablePlanets = 10
        numUraniumPlanets = self.numStars / 4
        numTitaniumPlanets = self.numStars / 2
        numWaterPlanets = self.numStars
        numHydrocarbonPlanets = self.numStars / 2
        numSiliconPlanets = self.numStars
        numDilithiumPlanets = self.numStars / 4
       
        samp_range = set((2,3,4,5,6,7))
        InhabitCount = 0
        for i in range(0,self.numStars):
            self[i].StoreDistances(self.StarList)
            for j in range(0,self[i].GetNumPlanets()):
               
                if numInhabitablePlanets+numWaterPlanets+numHydrocarbonPlanets+numTitaniumPlanets+numUraniumPlanets+numSiliconPlanets+numDilithiumPlanets == 0:
                    break
                #if numInhabitablePlanets == 0:
                    #samp_range -= set((1,0))
                if numUraniumPlanets == 0:
                    samp_range -= set((2,0))
                if numWaterPlanets == 0:
                    samp_range -= set((3,0))
                if numTitaniumPlanets == 0:
                    samp_range -= set((4,0))
                if numTitaniumPlanets == 0:
                    samp_range -= ((5,0))
                if numSiliconPlanets == 0:
                    samp_range -= set((6,0))
                if numDilithiumPlanets == 0:
                    samp_range -= set((7,0))
                luckynum = random.sample(samp_range,3)
                
                InhabitCount += self[i][j].SetResource(resdict[luckynum[0]])
                InhabitCount += self[i][j].SetResource(resdict[luckynum[1]])
                InhabitCount += self[i][j].SetResource(resdict[luckynum[2]])
                
        if InhabitCount < numInhabitablePlanets:
            difference = numInhabitablePlanets - InhabitCount
            seeds = random.sample(range(0,self.numStars),difference)
            try:
                for i in difference:
                    g[i][0].Inhabitable = 1 #star will always have 1 planet
            except:
                pass
