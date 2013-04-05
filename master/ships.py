#!/usr/bin/env python

#######################################################
# ships.py - Classes for all in game ships.
# Authors : Justin Sweitzer, Ben Sweitzer
# Started development 04/04/2013
# Version 0.1
#
#######################################################

import random

class CapitalShip():
    def __init__(self, VesselClass):
        if VesselClass == 'Explorer':  
            chas = 5
            turrets = 2
            MaxCores = 2
            WarpCores = 1
            MaxEngines = 2
            WarpEngines = 1
            enginetype = 'Nuclear'
            coretype = 'EM'
            
        self.MaxChassis = chas
        self.CurrentChassis = chas
        self.Fighters = Fighters
        self.WarpCores = [ components.WarpCore(coretype) for i in range(0,WarpCores) ]
        self.WarpEngines = [ components.WarpEngine(enginetype) for i in range(0,WarpEngines) ]
        self.PowerConsumption = sum(((self.WarpEngines[i].PowerConsumption*i^2) for i in range(0,WarpEngines))) 
        self.FuelCapacity = sum((self.WarpCores[i].Capacity for i in range(0,WarpCores)))
        
        self.MaxWarp = 
       

class Fighter():
    pass

class Frigate():
    pass

class Cruiser():
    pass

class Destroyer():
    pass

# The player will only have a capital ship that can be upgraded/upsized to various 'classes'
# Classes should be named something cool like 'Ticonderoga', etc.
# Fighter chassis launchable via capital ship, replace kamikaze/guided drone concept from Lightspeed with Torpedos.
# Should torpedos use a chassis?
# Individual components will be upgradable within the same 'class' of vessel

# The other types of vessels should be reserved for aliens. 
 