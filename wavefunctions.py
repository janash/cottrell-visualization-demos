import numpy as np
import itertools

def spherical_to_cartesian(r, theta, phi):
    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(phi) * np.sin(theta)
    z = r * np.cos(theta)
    
    return x, y, z

def cartesian_to_spherical(x, y, z):
    r = np.sqrt(x**2 + y**2 + z**2)
    phi = np.arctan2(y,x)
    theta = np.arctan2(np.sqrt(x**2+y**2),z)
    
    return r, theta, phi


def wavefunction(n, m, l):
    
    def wavefunction_100(r, theta=None, phi=None):
        return (1/np.sqrt(np.pi)) * np.exp(-r)

    def wavefunction_200(r, theta=None, phi=None):
        return (1/4)*(1/(np.sqrt(2*np.pi)))*(2 - r)*np.exp(-r)
    
    def wavefunction_210(r, theta, phi):
        return (1/(4*np.sqrt(2*np.pi)))*r*np.exp(-r/2)*np.cos(theta)

    def wavefunction_211(r, theta, phi):
        return 1/(4*np.sqrt(2*np.pi))*r*np.exp(-r/2)*np.sin(theta)*np.cos(phi)
    
    def wavefunction_21n1(r, theta, phi):
        return 1/(4*np.sqrt(2*np.pi))*r*np.exp(-r/2)*np.sin(theta)*np.sin(phi)
    
    def wavefunction_300(r, theta=None, phi=None):
        return (1/(81*np.sqrt(3*np.pi))*(27 - (18 * r) + 2 * r**2) * np.exp(-r/3))
        
    def wavefunction_310(r, theta, phi):
        return (1/81)*np.sqrt((2/np.pi))*(6*r - r**2)*np.exp(-r/3)*np.cos(theta)
        
    def wavefunction_311(r, theta,phi):
        return np.sqrt(2)/(81 * np.sqrt(np.pi))* (6 * r - r ** 2) * np.exp(-r/3) * np.sin(theta) * np.cos(phi)
        
    def wavefunction_31n1(r, theta, phi):
        return np.sqrt(2)/(81 * np.sqrt(np.pi))* (6 * r - r ** 2) * np.exp(-r/3) * np.sin(theta) * np.sin(phi)

    def wavefunction_320(r, theta, phi):
        return 1/(81*np.sqrt(6 * np.pi)) * r**2 * np.exp(-r/3) * (3*np.cos(theta)**2 - 1)
        
    def wavefunction_321(r, theta, phi):
        pass
    
    def wavefunction_32n1(r, theta, phi):
        pass


    wf_map = {
        (1, 0, 0) : wavefunction_100,
        (2, 0, 0) : wavefunction_200,
        (2, 1, 0) : wavefunction_210,
        (2, 1, 1) : wavefunction_211,
        (2, 1, -1) : wavefunction_21n1,
        (3, 0, 0) : wavefunction_300,
        (3, 1, 0) : wavefunction_310,
        (3, 1, 1) : wavefunction_311,
        (3, 1, -1): wavefunction_31n1,
        (3, 2, 0) : wavefunction_320,
        
    }
    
    try:
        return wf_map[(n,m,l)]
    except KeyError:
        raise NotImplementedError(f"Wavefunction for n={n}, m={m}, l={l} is not available.")