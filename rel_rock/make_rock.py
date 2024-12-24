import numpy as np

mass=1
C = 299792458
class relativistic_rock:
    def __init__(self, time_interval, length, speed):
        self.mass = mass
        self.length = length
        self.speed = speed
        self.time_interval = time_interval
        self.c = C
        
        if speed > C:
            raise ValueError("speed cannot exceed the speed of light")
            

    def relativistic_mass(self):
            return self.mass/np.sqrt(1-pow(self.speed,2)/pow(C,2))
        
    def relativistic_time(self):
            return self.time_interval/np.sqrt(1-pow(self.speed,2)/pow(C,2))
        
    def relativistic_length(self):
            return self.length *np.sqrt(1-pow(self.speed,2)/pow(C,2))
        
        
        
        
        

        
