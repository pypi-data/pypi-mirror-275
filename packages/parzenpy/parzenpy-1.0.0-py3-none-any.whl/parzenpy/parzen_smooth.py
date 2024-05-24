"""Class definition for parzenpy object."""

import numpy as np


class parzenpy:

    def __init__(self, freq, fft):

        """
        Function to apply smoothing to any Fast Fourier transform (fft)

        Parameters
        ----------

        freq: ndarray
            Array of frequency values from fft.
        fft: ndarray
            Array of amplitude values from fft.

        """

        self.freq = freq
        self.fft = fft

    @staticmethod
    def parzen_smooth(f, amp, fc, b=1.5, windowed_flag=True):

        """
        Function applies parzen smoothing to a fourier amplitude spectra (FAS)

        Parameters
        ----------

        f: ndarray
            Frequency array of the fft.
        amp: ndarray
            Amplitude of the fft.
        fc: ndarray
            resampled frequency in which to apply smoothing.
        b: float
            Smoothing parameter, larger values mean more smoothing. Default = 1.5
        windowed_flag: boolean
            Indicates whether the time series was separated into individual windows. Default = True

        returns a smoothed FAS using parzen smoothing

        """
        if windowed_flag:

            u = 151 * b / 280
            temp = np.pi * u * (f - fc[:, np.newaxis]) / 2
            filter_parzen = ((f > fc[:, np.newaxis] / b) & (f < fc[:, np.newaxis] * b) & (f != fc[:, np.newaxis]))
            weights = np.zeros((len(fc), len(f)))
            weights[filter_parzen] = np.power(np.sin(temp[filter_parzen]) / temp[filter_parzen], 4) * 3 / 4 * u
            weights[f == fc[:, np.newaxis]] = 1.0
            num = weights * amp[:, np.newaxis]
            smoothed = np.sum(num, axis=2) / np.sum(weights, axis=1)

        else:

            u = 151 * b / 280
            temp = np.pi * u * (f - fc[:, np.newaxis]) / 2
            filter_parzen = ((f > (fc[:, np.newaxis] / b)) & (f < (fc[:, np.newaxis] * b)) & (f != fc[:, np.newaxis]))
            weights = np.zeros((len(fc), len(f)))
            weights[filter_parzen] = (np.power(np.sin(temp[filter_parzen]) / temp[filter_parzen], 4) * 3 / 4 * u)
            weights[f == fc[:, np.newaxis]] = 1.0
            smoothed = np.sum(weights * amp, axis=1) / np.sum(weights, axis=1)

        return smoothed

    def apply_smooth(self, fc, b=1.5, windowed_flag=True):

        """
        Function that uses the parzen smoothing function to apply smoothing to FAS.

        Parameters
        ----------

        fc: ndarray
            Array of resampled frequencies to smooth.
        b: float
            Smoothing parameter, larger values mean more smoothing. Default = 1.5
        windowed_flag: boolean
            Indicates whether the time series was separated into individual windows. Default = True

        returns a smoothed FAS using the parzen smoothing function.

        """

        smoothed_fas = parzenpy.parzen_smooth(f=self.freq, amp=np.abs(self.fft), fc=fc, b=b,
                                              windowed_flag=windowed_flag)

        return smoothed_fas