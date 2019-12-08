# Mini Project: What is POPPY?

POPPY is a Python package that can create various forms of optical elements in order to analyze optics for space telescopes and other devices within the far and mid-field.

## What does POPPY do?

POPPY has many features for creating optical elements such as:
- Pupils/Apertures
- Aperture stops/Blocks
- Mirrors
- Thin lenses
- Image planes
- Wavefront errors
- Custom elements

What the library can do from there is generate a wavefront that propagates light through a created system and allows analysis of the simulated system. POPPY is capable of many different kinds of calculations, but it is most particularly invested in Fraunhofer (far-field) and Fresnel (mid-field) region diffraction. As such, it utilizes Fourier Transforms to calculate the transformation of light propagation from an aperture to an image plane.

## Types of Apertures

<p align="center"><img src="https://github.com/mysteriousmartel/poppyProject/blob/master/apertures.png"></img></p>

## Uses of POPPY in the field

This package was made by Marshall Perrin of the Space Telescope Science Institute. It was originally made for assisting with simulations of the James Webb Space Telescope, but is now utilized by optical engineers for various kinds of teloscopy and imaging involving point source functions (PSF).

Why this package means so much to myself and my collaborator is that it is an advanced version of our <a href="https://github.com/mbu54/601project">coded aperture project</a>.
