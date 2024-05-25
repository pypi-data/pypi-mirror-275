import scipy.stats as stats
import os
import pandas as pd
from pandas import DataFrame  as df
import numpy as np
from numpy import sqrt, pi

particle_dtype2d = np.dtype([('xi', 'f8'), ('r', 'f8'),
                             ('p_z', 'f8'), ('p_r', 'f8'), ('M', 'f8'),
                             ('q_m', 'f8'), ('q_norm', 'f8'), ('id', 'i8')])

# BEAM PROFILES

def Gauss(med=0, sigma=1, vmin=-1, vmax=0):
    def gauss_maker(N):
        p1 = 0 if vmin is None else stats.norm.cdf(vmin)
        p2 = 1 if vmax is None else stats.norm.cdf(vmax)
        return stats.norm.ppf(np.linspace(p1, p2, N+2)[1:-1], med, sigma)
    gauss_maker.med = med
    gauss_maker.sigma = sigma
    gauss_maker.f0 = 1. / sqrt(2*pi) / sigma
    return gauss_maker

def rGauss(sigma=1, vmin=0, vmax=1):
    def rgauss_maker(N):
        p1 = 0 if vmin is None else stats.weibull_min.cdf(vmin, 2) # cdf doesn't work properly
        p2 = 1 if vmax is None else stats.weibull_min.cdf(vmax, 2)
        # p1 = 0
        # p2 = 1
        # return sigma*np.sqrt(2.)*stats.weibull_min.ppf(np.linspace(p1, p2, N+2)[1:-1], 2)
        return stats.weibull_min.ppf(np.linspace(p1, p2, N+2)[1:-1], 2)
    rgauss_maker.med = 0
    rgauss_maker.sigma = sigma
    return rgauss_maker

def make_beam(config, xi_distr, pz_distr, Ipeak_kA,
              x_distr=None, y_distr=None, r_distr=None, px_distr=None, py_distr=None, ang_distr=None,
              q_m=1.0, partic_in_layer=200,
              savehead=False, saveto=False, name='beamfile.bin'):
        if q_m == 1 and Ipeak_kA > 0:
            print('Warning: Electrons must have negative current.')
            return

        if xi_distr.med > 0:
            print('Warning: Beam center is in xi>0.')

        # xi_step = config.getfloat('xi_step')

        if saveto and 'beamfile.bin' in os.listdir(saveto):
            raise Exception('Another beamfile.bin is found. You may delete it using the following command: "!rm %s".' % os.path.join(saveto, name))
        I0 = 17.03331478052319 # kA
        q = 2.*Ipeak_kA/I0/partic_in_layer
        gamma = pz_distr.med
        N = partic_in_layer / config.getfloat('xi-step') / xi_distr.f0
        N = int(round(N))
        xi = xi_distr(N)
        if savehead:
            xi = xi[xi >= -config.getfloat('window-length')]
            N = len(xi)
        else:
            xi = xi[(xi >= -config.getfloat('window-length')) & (xi <= 0)]
            N = len(xi)
        partic_in_mid_layer = np.sum((xi > xi_distr.med - config.getfloat('xi-step')/2) & (xi < xi_distr.med + config.getfloat('xi-step')/2))
        print('Number of particles:', N)
        print('Number of particles in the middle layer:', partic_in_mid_layer)
        xi = np.sort(xi)[::-1]

        if config.get('geometry') == 'c' or config.get('geometry') == 'circ':
            x = None
            y = None
            if r_distr is None:
                if x_distr is None:
                    raise Exception('Specify radial particle distribution.')
                elif y_distr is not None:
                    print('Generating r from x and y distributions')
                    x = x_distr(N)
                    np.random.shuffle(x)
                    y = y_distr(N)
                    np.random.shuffle(y)
                else:
                    print('Generating r from x distribution and y equal to x distribution')
                    x = x_distr(N)
                    np.random.shuffle(x)
                    y = x_distr(N)
                    np.random.shuffle(y)
                r = sqrt(x**2 + y**2)        
            else:
                r = np.abs(r_distr(N))
                np.random.shuffle(r)
            
            if ang_distr is None:
                if px_distr is None or x is None:
                    raise Exception('Specify angle or x, y distribution')
                elif py_distr is None:
                    print('Generating pr from px distribution and py equal to px distribution')
                    px = px_distr(N)
                    np.random.shuffle(px)
                    py = px_distr(N)
                    np.random.shuffle(py)
                else:
                    print('Generating pr from px and py distributions')
                    px = px_distr(N)
                    np.random.shuffle(px)
                    py = py_distr(N)
                    np.random.shuffle(py)
                pr = (x*px + y*py) / r
                M = sqrt(px**2 + py**2 - pr**2)
                        
            else:
                pr = gamma * ang_distr(N)
                np.random.shuffle(pr)
                M = gamma * ang_distr(N)
                np.random.shuffle(M)
            M = M * r    
            pz = pz_distr(N)
            np.random.shuffle(pz)
            
            particles = np.array([xi, r, pz, pr, M, q_m * np.ones(N), q * np.ones(N), np.arange(N)])
            stub_particle = np.array([[-100000., 0., 0., 0., 0., 1.0, 0., 0.]])
            beam_data = np.vstack([particles.T, stub_particle])
            #beam_data = np.array(beam_data.T, dtype=particle_dtype2d)
            #print(beam_data)
#             beam = df(beam, columns=['xi', 'r', 'pz', 'pr', 'M', 'q_m', 'q', 'N'])
        elif config.get('geometry') == '3d':
            x = x_distr(N)
            if y_distr is not None:
                y = y_distr(N)
            else:
                y = x_distr(N)
            np.random.shuffle(x)
            np.random.shuffle(y)
            pz = pz_distr(N)
            np.random.shuffle(pz)
            px = px_distr(N)
            if py_distr is not None:
                py = py_distr(N)
            else:
                py = px_distr(N)
            np.random.shuffle(px)
            np.random.shuffle(py)
            particles = np.array([xi, x, y, pz, px, py, q_m * np.ones(N), q * np.ones(N), np.arange(N)], dtype=float)
            stub_particle = np.array([[-100000., 0., 0., 0., 0., 0., 1.0, 0., 0.]])
            beam_data = np.vstack([particles.T, stub_particle])
            #beam_data = np.array(beam_data, dtype=particle_dtype3d)
#             beam = df(beam_data, columns=['xi', 'x', 'y', 'pz', 'px', 'py', 'q_m', 'q', 'N'])
        
#         head = beam[beam.eval('xi>0')]
#         beam = beam[beam.eval('xi<=0'.format(-config.getfloat('window-length')))]
#         head = beam_data[beam_data[0] > 0]
#         beam = beam_data[beam_data[0] <= 0]
        beam = beam_data
        if saveto:
            beam.values.tofile(os.path.join(saveto, name))
        if savehead:
            head.values.tofile(os.path.join(saveto, 'head-' + name))
        return beam