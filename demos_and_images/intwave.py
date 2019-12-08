import poppy
import numpy as np
import matplotlib.pyplot as plt
import logging
from astropy import units as u
logging.basicConfig(level=logging.WARNING)

np.seterr(divide='ignore', invalid='ignore')

osys = poppy.OpticalSystem()

osys.add_pupil(poppy.CircularAperture(radius=3))
osys.add_detector(pixelscale=0.010, fov_arcsec=5.0)

psf = osys.calc_psf(display_intermediates=True)

radius = 6.5/2 * u.m
lyot_radius = 6.5/2.5 *u.m
pixelscale = 0.060 *u.arcsec/u.pixel
osys = poppy.OpticalSystem(oversample=4)
pupil = poppy.CircularAperture(radius=radius)

occulter = poppy.CircularOcculter(radius = 0.1*u.arcsec)
# adjust display size and color scale after the occulter
occulter.wavefront_display_imagecrop = 1.0
occulter.wavefront_display_vmin_hint=1e-6

lyotstop = poppy.CircularAperture(radius=lyot_radius)
# hint that we would like to see intensity rather than phase after Lyot stop
lyotstop.wavefront_display_hint='intensity'

osys.add_pupil( pupil)
osys.add_image( occulter)
osys.add_pupil( lyotstop)
osys.add_detector(pixelscale=pixelscale, fov_arcsec=2.0)
# you can also set hints onto optics in the planes list
osys.planes[-1].wavefront_display_vmin_hint =  1e-6

plt.figure(figsize=(8,8))
psf = osys.calc_psf(wavelength = 1*u.micron, display_intermediates=True)

plt.savefig('intwave.png', dpi=100)