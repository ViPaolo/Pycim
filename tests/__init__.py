try:
    import numpy
    import PIL
    import os
    import sys
except ImportError as e:
    raise ImportError(f"Dipendenze mancanti: {e}. Installa i requisiti con 'pip install -r requirements.txt'")


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))



