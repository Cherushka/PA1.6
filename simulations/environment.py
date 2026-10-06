import math
from dataclasses import dataclass

@dataclass
class Environment:
    base: float = 5.0
    amplitude: float = 2.0
    period_s: float = 7200.0
    door_drop_C: float = 5.0
    door_start_s: float = 1200.0
    door_duration_s: float = 120.0

    def T_out(self, t: float) -> float:
        ''' Calculate the outside temperature at time t (seconds).
            The temperature follows a sinusoidal pattern with a specified base, amplitude, and period.
            Additionally, there is a temporary drop in temperature to simulate a door opening event.
            t: Time in seconds.
            Returns the outside temperature in degrees Celsius.
        '''
       # 1. Calculate the standard sinusoidal outside temperature
        # We use 2 * pi * (t / period) to correctly scale the time to a full sine wave cycle
        current_temp = self.base + self.amplitude * math.sin(2 * math.pi * (t / self.period_s))
        
        # 2. Check if a door drop event is currently happening
        end_time = self.door_start_s + self.door_duration_s
        if self.door_start_s <= t <= end_time:
            current_temp -= self.door_drop_C
            
        return current_temp
        