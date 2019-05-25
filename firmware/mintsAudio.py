import pyaudio
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import time
import sys
from matplotlib import style
from scipy.fftpack import fft

FORMAT = pyaudio.paInt16 # We use 16bit format per sample
CHANNELS = 1
RATE = 16000
CHUNK = 1024 # 1024bytes of data red from a buffer
INTERVAL = 1/RATE

audio = pyaudio.PyAudio()

# start Recording
stream = audio.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True)#,


def main():

    global keep_going
    keep_going = True

    stream.start_stream()

    startTime = time.time()
    while keep_going:
        try:
            stream.start_stream()
            yf = returnPowerSpectrum()
            maxInd = np.argmax(yf)
            xf = np.linspace(0.0, 1.0/(2.0*INTERVAL), CHUNK//2)
            xfr = [round(x,2) for x in xf]
            print(xfr)


            print(xf[maxInd])
            plt.plot(xf,yf)
            plt.pause(0.00001)
            plt.clf()
            stream.stop_stream()
        except KeyboardInterrupt:
            keep_going=False
        except:
            pass
    #
    # # Close up shop (currently not used because KeyboardInterrupt
    # is the only way to close)
    stream.stop_stream()
    stream.close()
    audio.terminate()


def returnPowerSpectrum():
    yf            = fft(np.fromstring(stream.read(CHUNK), np.int16))
    powerSpectrum = 2.0/CHUNK * np.abs(yf[0:CHUNK//2])
    return powerSpectrum




if __name__ == "__main__":
   main()
