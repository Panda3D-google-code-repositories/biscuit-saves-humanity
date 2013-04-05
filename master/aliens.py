#!/usr/bin/env python

import random

class Alien():
    def __init__(self, numStars):
        self.Hostility = 50
        self.TradeResources = []
        self.TradeComponents = []
        self.Name = 'Generic Alien'
        self.HomeSystem =  random.randint(0,numStars) 
        self.HomeSystemCoords = []  # Need a method for returning star coordinates with ID
        self.ColonySystems = []
        self.numColonies = random.randint(0,5)
        self.AllowPeaceTreaty = 0
        self.AttackEarth = 0
        self.AllowTrade = 1
        
    def SetName(self,name):
        self.Name = name
        
    def SetNumberofColonies(self,numColonies):
        self.numColonies = numColonies
        self.ColonySystems = []
        for i in range(0,numColonies):
            self.ColonySystems.append(self.HomeSystem+i)  # Need to sort starlist by coordinates so this will be the X closest systems.
        
    
    def PlayerInteraction(self,interaction):
        if interaction == 'Neutral Space Combat' or interaction == 'Destroyed Alien Ship':
            self.Hostility += 1
        elif interaction == 'Alien System Combat':
            self.Hostility += 3
        elif interaction == 'Destroyed Alien Base':
            self.Hostility += 10
        elif interaction == 'Trade Components':
            self.Hostility -= 1
        elif interaction == 'Trade Resources':
            self.Hostility -= 3
        elif interaction == 'Sign Peace Treaty' or interaction == 'Give Component Gift':
            self.Hostility -= 5
        elif interaction == 'Give Resource Gift':
            self.Hostility -= 7
        elif interaction == 'Player Fled Alien Initiated Combat':
            self.Hostility -= 5
            
        else:
            pass
        self.SetBehavior()
        
        # add more conditions that you can think of  
        
    def SetBehavior(self):        
        if self.Hostility <= 25:
            self.AllowPeaceTreaty = 1
        else:
            self.AllowPeaceTreaty = 0            
        if self.Hostility == 100:
            self.AttackEarth = 1
        else:
            self.AttackEarth = 0           
        if self.Hostility >= 65:
            self.AllowTrade = 0
        else:
            self.AllowTrade = 1
            
# I think I am going to take a different approach to this and make individual text files for each alien race.        
          
class Lagrangians(Alien):       # Derived classes of aliens... maybe implement some unique behavior for each.
    pass

class Eulerians(Alien):
    pass

class ALE(Alien):
    pass

class Snootians(Alien):
    pass

class Bohemians(Alien):
    pass
    

    
    

