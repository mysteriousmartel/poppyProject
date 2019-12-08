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


