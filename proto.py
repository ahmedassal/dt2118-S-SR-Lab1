# DT2118, Lab 1 Feature Extraction
# Functions to be implemented ----------------------------------
import numpy as np
from scipy.signal import lfilter
from scipy.fftpack import fft, dct
example = np.load('C:\Users\Linnea\Desktop\dt2118_lab1_2016-04-01\example.npz')['example'].item()
tidigits = np.load('C:\Users\Linnea\Desktop\dt2118_lab1_2016-04-01\etidigits.npz')['tidigits']

def enframe(samples, winlen, winshift):
    """
    Slices the input samples into overlapping windows.

    Args:
        winlen: window length in samples.
        winshift: shift of consecutive windows in samples
    Returns:
        numpy array [N x winlen], where N is the number of windows that fit
        in the input signal
    """
    
    # CONFUSE
    """
    chunks = []
    chunks = np.array([chunks])
    for x in range(0,len(samples),winshift):
        np.concatenate((chunks,samples[x:x+winlen]))
        #chunks.append(samples[x:x+winlen])
    #chunks=[samples[x:x+winlen] for x in range(0, len(samples), winshift)]
    return chunks
    """
def preemp(input, p=0.97):
    """
    Pre-emphasis filter.

    Args:
        input: array of speech frames [N x M] where N is the number of frames and
               M the samples per frame
        p: preemhasis factor (defaults to the value specified in the exercise)

    Output:
        output: array of pre-emphasised speech samples
    Note (you can use the function lfilter from scipy.signal)
    """
    return lfilter([1., -p], 1, input)

def windowing(input):
    """
    Applies hamming window to the input frames.

    Args:
        input: array of speech samples [N x M] where N is the number of frames and
               M the samples per frame
    Output:
        array of windoed speech samples [N x M]
    Note (you can use the function hamming from scipy.signal, include the sym=0 option
    if you want to get the same results as in the example)
    """

def powerSpectrum(input, nfft):
    """
    Calculates the power spectrum of the input signal, that is the square of the modulus of the FFT

    Args:
        input: array of speech samples [N x M] where N is the number of frames and
               M the samples per frame
        nfft: length of the FFT
    Output:
        array of power spectra [N x nfft]
    Note: you can use the function fft from scipy.fftpack
    """
    transformed = fft(input,nfft)
    return pow(abs(transformed),2)

def logMelSpectrum(input, samplingrate):
    """
    Calculates the log output of a Mel filterbank when the input is the power spectrum

    Args:
        input: array of power spectrum coefficients [N x nfft] where N is the number of frames and
               nfft the length of each spectrum
        samplingrate: sampling rate of the original signal (used to calculate the filterbanks)
    Output:
        array of Mel filterbank log outputs [N x nmelfilters] where nmelfilters is the number
        of filters in the filterbank
    Note: use the trfbank function provided in tools.py to calculate the filterbank shapes and
          nmelfilters
    """

def cepstrum(input, nceps):
    """
    Calulates Cepstral coefficients from mel spectrum applying Discrete Cosine Transform

    Args:
        input: array of log outputs of Mel scale filterbank [N x nmelfilters] where N is the
               number of frames and nmelfilters the length of the filterbank
        nceps: number of output cepstral coefficients
    Output:
        array of Cepstral coefficients [N x nceps]
    Note: you can use the function dct from scipy.fftpack.realtransforms
    """
    cosTrans = dct(input, norm = 'ortho')
    return np.array(cosTrans)[:,0:nceps]

def dtw(localdist):
    """Dynamic Time Warping.

    Args:
        localdist: array NxM of local distances computed between two sequences
                   of length N and M respectively

    Output:
        globaldist: scalar, global distance computed by Dynamic Time Warping
    """
