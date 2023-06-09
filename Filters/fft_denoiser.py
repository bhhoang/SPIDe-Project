import scipy
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import matplotlib.image as mpimg
from scipy.fftpack import fft2, fftfreq, fftshift, ifft2
from scipy import ndimage


def spectrum_plot(img_fft):
    # Plotting spectrum
    plt.figure("Spectrum")
    plt.imshow(np.abs(img_fft), norm=LogNorm(vmin=5))
    plt.colorbar()
    plt.title('Fourier transform')
    plt.xlabel('kx')
    plt.ylabel('ky')
    plt.show()


# Filter in FFT
def filter_fft(img_fft):
    keep_fraction = 0.1  # The greater this value, the more pixels are preserved (0.1 = 10%) which means less noise is removed
    im_fft2 = img_fft.copy()
    r, c = im_fft2.shape
    im_fft2[int(r * keep_fraction):int(r * (1 - keep_fraction))] = 0
    im_fft2[:, int(c * keep_fraction):int(c * (1 - keep_fraction))] = 0
    plt.figure("Filtered spectrum")
    plt.imshow(np.abs(im_fft2), norm=LogNorm(vmin=5))
    plt.colorbar()
    plt.title('Filtered Fourier transform')
    plt.xlabel('kx')
    plt.ylabel('ky')
    plt.show()
    return im_fft2


def denoiser(img):
    # Inverse Fourier transform
    im_fft2 = fft2(img)
    result = filter_fft(im_fft2)
    img_new = ifft2(result).real
    return img_new
