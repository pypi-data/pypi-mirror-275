# parzenpy

A python library that perform Parzen spectral smoothing using numpy vectorized operations very efficiently.

# Background

A Parzen window also known as a Kernel Density Estimation function which was developed by Emanuel Parzen (see reference)

> E. Parzen, “Mathematical Considerations in the Estimation of Spectra”, Technometrics, Vol. 3, No. 2 (May, 1961), pp. 167-    190.

is a non-parametric estimation method that can apply smoothing by fitting a 4th order spline window to frequency spectra. In this case we apply the function to smooth Fourier Amptlitude Spectra (FAS).

# Installation
parzenpy is available using pip and can be installed with:

`pip install parzenpy`

# Usage

A user can smooth a seismic signal using a the function apply_smoothing using a bandwidth of 1.5. Larger values will return greater smoothing

`import parzenpy
smooth_fas = parzenpy.apply_smooth(freq, fft, fc, b=1.5, windowed_flag=True)`

# Citation

>Francisco-Javier Ornelas. (2024). fjornelas/parzenpy: latest(concept). Zenodo. (waiting on DOI)

