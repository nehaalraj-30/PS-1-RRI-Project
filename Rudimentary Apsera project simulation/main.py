import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from sine_input import sine_curve
from window import window
from adc import sample,adc

n_bits = 12
v_ref = 3.3
f = 2e8
sampling_rate = 1e12 #in hz not our adc sample
adc_sampling_rate = 4e9
fft_points = 16*2**10
duration = fft_points/adc_sampling_rate
time,vin_values = sine_curve(f,sampling_rate,duration,v_ref)
adc_time,adc_signal = sample(time,adc_sampling_rate,vin_values)
digital_values = [adc(vin,n_bits,v_ref) for vin in adc_signal]

w_signal,w_time = window(digital_values,adc_time)

plt.plot(adc_time, adc_signal,linestyle = 'dashed')
plt.xlabel('t(us)')
plt.ylabel('amplitude')
plt.title('signal')
plt.grid(True)
plt.savefig("input_main.png")
plt.close()

plt.step(adc_time*1e6, digital_values, where ='post')
plt.xlabel('time(us)')
plt.ylabel('Digital Output (Decimal)')
plt.title(f'{n_bits}-bit ADC Conversion')
plt.grid(True)
# plt.xlim(1,1.05)
plt.savefig("adc_main.png")

plt.step(w_time*1e6,w_signal,where = 'post')
plt.xlabel('t(us)')
plt.ylabel('amplitude')
plt.title('windowed_signal')
plt.grid(True)
# plt.xlim(1,1.05) 
plt.savefig("windowed_main.png")


