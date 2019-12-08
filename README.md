# Mini Project: What is POPPY?

<a href="https://poppy-optics.readthedocs.io/en/stable/index.html#">POPPY</a>

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

Why this package means so much to myself and my collaborator is that it is an advanced version of our <a href="https://github.com/mbu54/601project">coded aperture project</a>. We have since learned that there are other Python packages out there that are working to simulate wavefront propagation as well as convolve apertures with objects to reconstruct images.

## Limitations of the library

Since it has to deal with large calculations depending on the size of your simluation, memory is a big issue with running POPPY. For the installation alone, a hybrid gaming laptop was unable to install all parts for running the full extent of the library's processing ability, and is only able to run up to mid-tier computations.

## Collaborators, references, and other info

For this project, I worked with Merlin Hoffman under approval from our professor. He originally found this Python package, and we used my computer to get it to run and demonstrate how the code works.
