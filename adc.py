import matplotlib.pyplot as plt
import numpy as np

## setup input as sine_curve and fit into adc range
def sine_curve(f,sampling_rate,duration,v_ref,noise_factor):
    n_samples = int(duration*sampling_rate)
    t = np.linspace(0,duration,n_samples, endpoint= False)
    noise = noise_factor*np.random.normal(0,0.09,t.shape)
    scaling_factor = 1
    sine_sig = noise + scaling_factor*(np.sin(2*np.pi*(f)*t.astype(np.float64))+1)*(v_ref/2)
    
    return t,sine_sig

# sample sine curve 
def sample(time,adc_sampling_rate,signal):
    step = int(len(time) / (adc_sampling_rate*(time[-1]-time[0]))) #no.of samples in x time duration
    return time[::step],signal[::step]

def adc(vin, n_bits, v_ref):
    vin_clipped = np.clip(vin,0,v_ref)
    return int(np.floor((vin_clipped/v_ref)*(2**n_bits-1)))

n_bits = 12
v_ref = 3.3
f = 2e8
noise_factor
sampling_rate = 1e12 #in hz,not our adc sample
adc_sampling_rate = 4e9
time_period = 10
duration = time_period*(1/f)
time,vin_values = sine_curve(f,sampling_rate,duration,v_ref,noise_factor)
adc_time,adc_signal = sample(time,adc_sampling_rate,vin_values)
digital_values = [adc(vin,n_bits,v_ref) for vin in adc_signal]

plt.plot(adc_time*1e9, adc_signal,linestyle = 'dashed')
plt.xlabel('t(ns)')
plt.ylabel('amplitude')
plt.title('signal_sampled')
plt.grid(True)
plt.savefig("input_adc_sampled.png")

plt.plot(time*1e9, vin_values)
plt.xlabel('t(ns)')
plt.ylabel('amplitude')
plt.title('signal')
plt.grid(True)
plt.savefig("input_adc.png")


    
plt.step(adc_time*1e9, digital_values, where='post')
plt.xlabel('time')
plt.ylabel('Digital Output (Decimal)')
plt.title(f'{n_bits}-bit ADC Conversion')
plt.grid(True)
plt.savefig("adc.png")



    
