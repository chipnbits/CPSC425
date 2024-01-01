"""
Image Processing Utilities

This module, `util.py`, contains a collection of utility functions for image processing tasks in CPSC425. 

Functions:
    - array_to_image(a): Converts a numpy array to a PIL Image.
    - image_to_array(image): Converts a PIL Image to a numpy array.
    - rescale_image(image, scale_factor): Rescales a PIL Image by a given scale factor.

Author: Simon Ghyselincks
Created: December 30, 2023

Usage:
    This module is intended to be imported and used in other Python scripts for image processing tasks.
    Example:
        from util import rescale_image

Dependencies:
    - PIL (Pillow)
    - numpy
"""

from PIL import Image
import numpy as np

def array_to_image(a):
    """Converts a numpy array to a PIL Image with pixel clipping.
    
    Args:
        a: The numpy array to convert.
        
    Returns:
        PIL.Image: The converted PIL Image.

    """
    a = np.clip(a, 0, 255)  # clip to [0,255] to prevent overflows
    return Image.fromarray(np.uint8(a))

def image_to_array(image):
    """Converts a PIL Image to a numpy array.
    
    Args:
        image (PIL.Image): The PIL Image to convert.
        
    Returns:
        numpy.ndarray: The converted numpy array.

    """
    return np.asarray(image, dtype='float32')

def rescale_image(image, scale_factor):
    """Rescale the given PIL Image by the scale factor.

    Args:
        image (PIL.Image): The image to rescale.
        scale_factor (float): The factor to scale the image by.

    Returns:
        PIL.Image: The rescaled image.
    """
    # Calculate the new size
    new_width = int(image.width * scale_factor)
    new_height = int(image.height * scale_factor)
    new_size = (new_width, new_height)

    # Resize the image
    rescaled_image = image.resize(new_size, Image.BICUBIC)

    return rescaled_image





