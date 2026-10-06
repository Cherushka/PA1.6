from typing import Optional
from utils.rng import RNG

def step_room(T: float, heater_on: int, T_out: float, R: float, C: float, P: float,
              dt: float, process_sigma: float = 0.0, rng: Optional[RNG] = None) -> float:
    ''' Simulate one time step of a simple RC room thermal model.
        T: Current room temperature (degrees Celsius).
        heater_on: Heater state (0=OFF, 1=ON).
        T_out: Outside temperature (degrees Celsius).
        R: Thermal resistance (degrees Celsius per Watt).
        C: Thermal capacitance (Joules per degrees Celsius).
        P: Heater power when ON (Watts).
        dt: Time step duration (seconds).
        process_sigma: Standard deviation of process noise (degrees Celsius).
        rng: Optional random number generator for noise.
        Returns the updated room temperature after time step dt.
    '''
    # 1. Calculate the rate of temperature change (dT/dt)
    dTdt = (T_out - T) / (R * C) + (heater_on * P) / C
        
    # 2. Apply Euler integration to find the new temperature after dt seconds
    T_new = T + (dTdt * dt)
        
    # 3. Add process noise if an RNG and a valid standard deviation are provided
    if rng is not None and process_sigma > 0.0:
        # Assuming the provided RNG class uses a standard numpy-style 'normal' method 
        # for drawing from a Gaussian distribution
        T_new += rng.normal(0.0, process_sigma)
            
    return T_new
