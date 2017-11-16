import soundfile as sf
import sounddevice as sd
import matplotlib.pyplot as plt

path = "I:/Data/EnergyMarket_Trading1Week/Trading Analysis/RAELR\Py/mir/"
filename = "Flute.nonvib.ff.G4.stereo.aif"
data, fs = sf.read(path + filename)
sd.play(data, fs)

plt.plot(data[80000:81000])