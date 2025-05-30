import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def window(digital_values,adc_time):
    digital_values = digital_values[:16*2**10]
    windowed_time = adc_time[:16*2**10]
    w = signal.windows.hann(len(digital_values))
    windowed_signal = w * digital_values
   # windowed_signal = windowed_signal/np.sum(w) 
    
    return windowed_signal,windowed_time
