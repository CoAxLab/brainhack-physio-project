def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    # fs, lowcut and highcut are in frequency units (Hz)
    from scipy.signal import (sosfilt, butter)
    
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    sos = butter(order, [low, high], analog=False, btype='band', output='sos')
 
    y = sosfilt(sos, data)
    return y

def gaussian_lowpass_filter(data, fs, fwhm):
    # sampling rate is frequency (in Hz)
    # fwhm is time (in seconds)
    
    from scipy.ndimage import gaussian_filter1d
    
    sigma = fs*fwhm # 
    return gaussian_filter1d(data, sigma)
