from PIL import Image
from pycim.steg import  Decode_Image, Encode_Image

def main():
    image = Image.open(r".\tests\Lena.png")
    image.show()

    text = " Hello honey. ãìꜗꜗꜗ"

    new_image = Encode_Image(image, text)
    print(type(new_image))
    new_image.show()

    decoded_message = Decode_Image(new_image)
    print(decoded_message)
    return decoded_message

if __name__ == "__main__":
    main()
