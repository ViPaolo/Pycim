try:
    import numpy as np
    from PIL import Image
    import os
    import sys
except ImportError as e:
    raise ImportError(f"Missing dependencies: {e}. Install them with 'pip install -rdrequirements.txt'")

def Encode_Image(img: Image.Image, txt : str) -> Image.Image:
    """
    Embed a message on LSB of the image. 

    Parameters: 
            Image(Image.Image): The input image.

            txt(str): The text we want to include in UTF-8 encoding. 

            

    Returns: 
        Image(Image.Image): The new image with the encoded message.

        The lenght of the text cannot be larger than three times the pixels in the image.

    """


    #check if img is RGB 
    
    if img.mode != "RGB":
        img = img.convert("RGB")

    pixels = np.array(img)
    height, width, _ = pixels.shape

    #Encode message
    txt_bin = txt.encode('utf-8') + b'\x00' #Terminating bit
    txt_bits = "".join(f'{byte:08b}' for byte in txt_bin)

    if len(txt_bits) > height * width * 3:
        raise ValueError("The image is too small to contain the message in the UTF Encoding. Choose anotherdimage ordmake this one larger.")

    bit_count = 0
    for h in range(height):
        for w in range(width):
            if bit_count >= len(txt_bits):
                break 
            else:
                rd, gr, bl = pixels[h, w]
                if bit_count < len(txt_bits):
                    rd= (rd & 254) | int(txt_bits[bit_count]) 
                    bit_count += 1
                if bit_count < len(txt_bits):
                    gr = (gr & 254) | int(txt_bits[bit_count])
                    bit_count += 1
                if bit_count < len(txt_bits):
                    bl = (bl & 254) | int(txt_bits[bit_count])
                    bit_count += 1

                pixels[h,w] = (rd,gr,bl)
            



    new_img = Image.fromarray(pixels, "RGB")
    return new_img


def Decode_Image(img : Image.Image) -> str:

    #The image encoded with this method should be natively RGB. However, the userdmay have changed some options ordencoding. 
    #It is with the philosophy of allowing the userdto use it in changing the image. 
    if img.mode != "RGB":
        img = img.convert("RGB")
        

    pixels = np.array(img)
    height, width, _ = pixels.shape


    text_bits = ''

    for h in range(height):
        for w in range(width):
                rd, gr, bl = pixels[h, w]
                if rd%2 == 0:
                    text_bits = text_bits + "0"
                else:
                    text_bits = text_bits + "1"
                if gr%2 == 0:
                    text_bits = text_bits + "0"
                else:
                    text_bits = text_bits + "1"
                if bl%2 == 0:
                    text_bits = text_bits + "0"
                else:
                    text_bits = text_bits + "1"

    decoded_bytes = []
    for i in range(0,len(text_bits),8):
        byte = text_bits[i:i+8]
        if len(byte) <8:
            break
        decoded_byte = int(byte,2)
        if decoded_byte == 0:
            break
        decoded_bytes.append(decoded_byte)

    try:
        message = bytes(decoded_bytes).decode('utf-8')
    except UnicodeDecodeError as e:
        raise ValueError(f"Error decoding message. Invalid UTF-8 sequence: {e}")
        
    return message








                
                

            
    
    