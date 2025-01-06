from PIL import Image
from pycim.steg import _Normalize_Image, Encode_Image

def main():
    image = Image.open(r".\tests\Lena.png")
    new_image = _Normalize_Image(image)
    # new_image.show()

    text = "ciao"

    trial = Encode_Image(image, text)
    print(type(trial))

    return None

if __name__ == "__main__":
    main()
