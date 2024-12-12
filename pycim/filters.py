from PIL import Image, ImageOps
import numpy as np

def apply_negative(image : Image.Image, mode : str = "color" ) -> Image.Image:
    """
    Apply a negative filter to the given image.

    Parameters: 
        Image(Image.Image): The input image.



    Returns:
        Image.Image: The negative of the input image.
    """


    if not isinstance(image, Image.Image):
        raise ValueError("Input must be a PIL.Image.Image object")
    
    # Convert image to numpy array

    img_array = np.array(image)

    if mode == "color":
        #invert color image
        negative = 255 - img_array
    elif mode == "grayscale":
        # Convert to grayscale first, then invert
        grayscale = np.dot(img_array[...,:3], [0.2989, 0.5870, 0.1140])
        negative = 255 - grayscale
    else:
        raise ValueError("Mode must be 'color' or 'grayscale'. ")

    # Convert back to Pil Image
    return Image.fromarray(negative.astype(np.uint8))