import PIL.Image


try:
    import numpy as np
    import PIL
    import os
    import sys
except ImportError as e:
    raise ImportError(f"Missing dependencies: {e}. Install them with 'pip install -r requirements.txt'")

def _Normalize_Image(img: PIL.Image.Image) -> PIL.Image.Image:
    """
    Takes an image and returns its normalized version for LSB stenography. 
    Used for Encoding text into image, otherwise use other functions.
    """

    new_img = PIL.Image.eval(img, (lambda x: x if x%2 == 0 else x-1 ))
    return new_img


def Encode_Image(img: PIL.Image, txt : str) -> PIL.Image:
    """
    
    """


    #check if img is RGB 
    
    if img.mode != "RGB":
        img = img.convert("RGB")
    
    
    img = _Normalize_Image(img)

    pixels = np.array()
    height, width, _ = pixels.shape()

    #Encode message
    txt_bin = txt.encode('utf-8') + b'\x00' #Terminating bit
    txt_bits = "".join(f'{byte:08b}' for byte in txt_bin)

    if len(txt_bits) > height * width * 3:
        raise ValueError("The image is too small to contain the message in the UTF Encoding. Choose another image or make this one larger.")

    bit_count = 0
    for h in range(height):
        for w in range(width):
            if bit_count >= len(txt_bits):
                break 
            else:
                r, g, b = pixels[h, w]
                if bit_count < len(txt_bits):
                    r = r | int(txt_bits[bit_count]) 
                    bit_count += 1
                if bit_count < len(txt_bits):
                    g = g | int(txt_bits[bit_count])
                    bit_count += 1
                if bit_count < len(txt_bits):
                    b = b | int(txt_bits[bit_count])
                    bit_count += 1

                pixels[h,w] = (r,g,b)
            



    new_img = PIL.Image.fromarray(pixels, "RGB")
    return new_img



    return txt