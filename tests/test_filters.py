import pytest
import os
import numpy as np
from PIL import Image
from .filters import apply_negative

def test_apply_negative():
    # Create a test image
    test_image = Image.fromarray(np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8))
    test_image_path = 'test_image.jpg'
    test_image.save(test_image_path)
    
    # Apply negative transformation
    negative_image = apply_negative(test_image_path)
    
    # Assertions
    assert isinstance(negative_image, Image.Image)
    
    # Convert to numpy for detailed checks
    negative_array = np.array(negative_image)
    original_array = np.array(test_image)
    
    # Check if truly negative (pixel values inverted)
    assert np.all(negative_array == 255 - original_array)
    
    # Clean up test image
    import os
    os.remove(test_image_path)