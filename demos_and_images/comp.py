import poppy
import numpy as np
import matplotlib.pyplot as plt
import logging
logging.basicConfig(level=logging.DEBUG)

np.seterr(divide='ignore', invalid='ignore')
osys = poppy.OpticalSystem()
osys.add_pupil(poppy.CircularAperture(radius=3))    # pupil radius in meters
osys.add_detector(pixelscale=0.010, fov_arcsec=5.0) 

plt.figure(figsize=(16,12))

ap = poppy.MultiHexagonAperture(rings=3, flattoflat=2)           # 3 rings of 2 m segments yields 14.1 m circumscribed diameter
sec = poppy.SecondaryObscuration(secondary_radius=1.5, n_supports=4, support_width=0.1)   # secondary with spiders
atlast = poppy.CompoundAnalyticOptic( opticslist=[ap, sec], name='Mock ATLAST')           # combine into one optic

atlast.display(npix=1024, colorbar_orientation='vertical')
plt.savefig('example_atlast_pupil.png', dpi=100)

plt.figure(figsize=(8,6))

osys = poppy.OpticalSystem()
osys.add_pupil(atlast)
osys.add_detector(pixelscale=0.010, fov_arcsec=2.0)
psf = osys.calc_psf(1e-6)

poppy.display_psf(psf, title="Mock ATLAST PSF")
plt.savefig('example_atlast_psf.png', dpi=100)

