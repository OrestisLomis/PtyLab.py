import numpy as np
from .fft import fft2c, ifft2c

def fresnelPropagator(u,z,wavelenght,L):
    k = 2 * np.pi /wavelenght
    #source coordinates, this assumes that the field is NxN pixels
    N = u.shape[-1]
    dx = L / N
    x = np.arange(-N / 2, N / 2) * dx
    [Y, X] = np.meshgrid(x,x)

    #target coordinates
    dq = wavelenght *z / L;
    q = np.arange(-N / 2, N / 2) * dq
    [Qy, Qx] = np.meshgrid(q,q);

    #phase terms
    Qin = np.exp(1j * k / (2 * z) * (np.square(X) + np.square(Y)) )
    #Qout = exp(1i * k / (2 * z) * (Qx. ^ 2 + Qy. ^ 2));
    #r = Qout. * fft2c(Qin. * u)
    r = fft2c(Qin * u)
    return r, dq, q, Qx, Qy

def angularSpectrumPropagator():
    raise NotImplementedError

def ft2():
    raise NotImplementedError

def ift2():
    raise NotImplementedError

def generateFresnelIR():
    raise NotImplementedError

def inverseTwoStepPropagator():
    raise NotImplementedError

def scaledASP():
    raise NotImplementedError

def scaledSPinv():
    raise NotImplementedError

def two_step_prop():
    raise NotImplementedError