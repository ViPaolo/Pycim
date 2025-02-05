try:
    import numpy
    import PIL
    import os
    import sys
except ImportError as e:
    raise ImportError(f"Missing dependency: {e}. Install requirements with 'pip install -r requirements.txt'")


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))



