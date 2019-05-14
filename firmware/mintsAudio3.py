
from scipy import signal
import matplotlib.pyplot as plt

import numpy as np
# try:
#     import pyaudio
#     import numpy as np
#     import pylab
#     import matplotlib.pyplot as plt
#     from scipy.io import wavfile
#     import time
#     import sys
#     import seaborn as sns
# except:
#     print "Something didn't import"



np.random.seed(1234)

fs = 10e3
N = 1e5
amp = 2*np.sqrt(2)
freq = 1234.0
noise_power = 0.001 * fs / 2
time = np.arange(N) / fs
x = amp*np.sin(2*np.pi*freq*time)
x += np.random.normal(scale=np.sqrt(noise_power), size=time.shape)


print(x)


f, Pxx_den = signal.welch(x, fs, nperseg=1024)

print(f)

print(Pxx_den)

plt.semilogy(f, Pxx_den)
plt.ylim([0.5e-3, 1])
plt.xlabel('frequency [Hz]')
plt.ylabel('PSD [V**2/Hz]')
plt.show()


np.mean(Pxx_den[256:])

f, Pxx_spec = signal.welch(x, fs, 'flattop', 1024, scaling='spectrum')
plt.figure()
plt.semilogy(f, np.sqrt(Pxx_spec))
plt.xlabel('frequency [Hz]')
plt.ylabel('Linear spectrum [V RMS]')
plt.show()

np.sqrt(Pxx_spec.max())


x[int(N//2):int(N//2)+10] *= 50.
f, Pxx_den = signal.welch(x, fs, nperseg=1024)
f_med, Pxx_den_med = signal.welch(x, fs, nperseg=1024, average='median')
plt.semilogy(f, Pxx_den, label='mean')
plt.semilogy(f_med, Pxx_den_med, label='median')
plt.ylim([0.5e-3, 1])
plt.xlabel('frequency [Hz]')
plt.ylabel('PSD [V**2/Hz]')
plt.legend()
plt.show()
