from scipy.signal import butter, filtfilt
from scipy import signal

# Create a notch filter to remove 50Hz component
def create_notch_filter(frequency, sample_rate, Q=10):
    nyquist = sample_rate / 2.0
    notch_freq = frequency / nyquist
    b, a = signal.iirnotch(notch_freq, Q)
    return b, a

# Apply the notch filter to remove 50Hz component
def remove_50Hz(data, sample_rate):
    b, a = create_notch_filter(50, sample_rate)
    filtered_data = signal.filtfilt(b, a, data)
    return filtered_data

def remove_xHz(data, sample_rate, filterFrequency):
    b, a = create_notch_filter(filterFrequency, sample_rate)
    filtered_data = signal.filtfilt(b, a, data)
    return filtered_data

def butter_lowpass(cutoff, fs, order=5):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = filtfilt(b, a, data)
    return y

def getOffset(data):
    OFFSET = 2
    while(data[OFFSET]!=10): #Check for linefeed
        OFFSET+=1
    OFFSET+=1
    return OFFSET

def getAdcVals(data, offset, ADCValues):
    AdcNum = data[offset + 0]
    if(AdcNum > 2):
        print("invalid ADC num")
        while(data[offset]!=0x0A):
            offset+=1
        offset+=1
    else:
        channels=[]
        for i in range(4):
            channels.append(data[offset + 1+3*i] * 2**16 + data[offset + 2+3*i] * 2**8 + data[offset + 3+3*i])
            if(channels[i] > 2**23):
                channels[i] = channels[i] - 2**24
            try:
                ADCValues[i+4*AdcNum].append(channels[i])
            except:
                pass
    return ADCValues, offset
