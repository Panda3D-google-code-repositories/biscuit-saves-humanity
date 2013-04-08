#!/usr/bin/env python

#######################################################
# aliens.py - Alien species descriptions.
# Authors : Justin Sweitzer, Ben Sweitzer
# Started development 04/04/2013
# Version 0.1
#
#######################################################

import random

class Alien():
    def __init__(self, StarList, fname):
        self.Hostility = 50
        self.TradeResources = []
        self.TradeComponents = []
        self.FriendlyGreeting =[]
        self.AngryGreeting =[]
        self.Name = 'Generic Alien'
        if fname != 0:
            self.SetAttributesFromFile(fname)
        self.HomeSystem =  random.randint(0,len(StarList))
        self.HomeStar = StarList[self.HomeSystem]
        self.HomeStar.SetInhabitants(self.Name,'Homeworld')
        self.HomeSystemCoords = self.HomeStar.Coordinates  # Need a method for returning star coordinates with ID
        self.ColonySystems = []
        self.numColonies = random.randint(1,7)
        self.AllowPeaceTreaty = 0
        self.AttackEarth = 0
        self.AllowTrade = 1
        self.SetNumberofColonies(self.numColonies)

       
    def SetAttributesFromFile(self,fname):
        f1 = open(fname,'r')
        allLines = f1.readlines()
        f1.close()
        for line in allLines:
            if 'Name' in line:
                self.Name = line.strip().split('=')[1]
            elif 'Hostility' in line:
                self.Hostility = line.strip().split('=')[1]
            elif 'TradeResources' in line:
                self.TradeResources = line.strip().split('=')[1].split(',')
            elif 'TradeComponents' in line:
                self.TradeComponents = line.strip().split('=')[1].split(',')
            elif 'FriendlyGreeting' in line:
                self.FriendlyGreeting.append(line.strip().split('=')[1])
            elif 'AngryGreeting' in line:
                self.AngryGreeting.append(line.strip().split('=')[1])
            else: 
                pass
       
    def SetNumberofColonies(self,numColonies):
        self.numColonies = numColonies
        self.ColonySystems = []
        DistanceList = self.HomeStar.DistanceList[1:]
        for i in range(0,numColonies):
                                    #  Star ID number,   Star Object
            self.ColonySystems.append([DistanceList[i][1],DistanceList[i][2]])  # Hopefully these are the X closest systems       
            DistanceList[i][2].SetInhabitants(self.Name,'Colony %i' % (i))
            
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