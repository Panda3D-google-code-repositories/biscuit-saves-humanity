#!/usr/bin/env python

#######################################################
# ships.py - Classes for all in game ships.
# Authors : Justin Sweitzer, Ben Sweitzer
# Started development 04/04/2013
# Version 0.1
#
#######################################################

import components, time

class Fighter():
    pass

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
            HitPoints = 20
        self.HitPoints = HitPoints
  #      self.MainGunPower = 
        self.Class = VesselClass   
        self.MaxChassis = chas
        self.CurrentChassis = chas
  #      self.Fighters = Fighters
  #      self.WarpCores = [ components.WarpCore(coretype) for i in range(0,WarpCores) ]
  #      self.WarpEngines = [ components.WarpEngine(enginetype) for i in range(0,WarpEngines) ]
  #      self.PowerConsumption = sum(((self.WarpEngines[i].PowerConsumption*i^2) for i in range(0,WarpEngines)))
  #      self.FuelCapacity = sum((self.WarpCores[i].Capacity for i in range(0,WarpCores)))
        self.MaxWarp = 9.9
        self.CurrentWarpFactor = 0
        self.Coordinates = (0.0,0.0,0.0)
        
    def WarpToSystem(self,System,WarpFactor):
        if WarpFactor > self.MaxWarp:
            print "Warp factor out of range of current capabilities"
        else:    
            distance = (sum((self.Coordinates[i] - System.Coordinates[i])**2 for i in range(0,3)))**0.5
            timetaken = int((distance/17320.51)*(WarpFactor/9.9)*30) 
            print 'Initializing warp engines'
            self.CurrentWarpFactor = WarpFactor
            time.sleep(1)
            print 'Current velocity is warp %f' % (self.CurrentWarpFactor)
            print 'Warping'
            for i in range(0,timetaken):
                print '.'
                time.sleep(1)
            print 'Arriving at coordinates %s, %s' % (System.Coordinates, System.Name)
            self.System = System
            self.Coordinates = self.System.Coordinates
            

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
 