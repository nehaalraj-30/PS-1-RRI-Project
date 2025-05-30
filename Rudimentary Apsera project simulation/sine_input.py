import numpy as np

def sine_curve(f,sampling_rate,duration,v_ref):
    n_samples = int(duration*sampling_rate)
    t = np.linspace(0,duration,n_samples, endpoint= False)
    noise = 0*np.random.normal(0,0.09,t.shape)
    scaling_factor = 1
    sine_sig = noise + scaling_factor*(np.sin(2*np.pi*(f)*t.astype(np.float64))+1)*(v_ref/2)

    
    return t,sine_sig

