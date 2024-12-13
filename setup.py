from setuptools import setup, find_packages

# Read the content of README.md
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pycim",  # Replace with your project name
    version="0.1.0",  # Initial version
    author="PIPPO",  # Replace with your name or team name
    author_email="your.email@example.com",  # Your contact email
    description="A Python library for image processing with filters and transformations.",
    long_description=long_description,
    long_description_content_type="text/markdown",  # Use Markdown format
    url="https://github.com/yourusername/pycim",  # Replace with the project's GitHub URL
    packages=find_packages(),  # Automatically finds your package folders
    install_requires=[
        "colorama==0.4.6",
        "coverage==7.6.9",
        "iniconfig==2.0.0",
        "numpy==2.2.0",
        "opencv-python==4.10.0.84",
        "packaging==24.2",
        "pillow==11.0.0",
        "pluggy==1.5.0",
        "pytest==8.3.4",
        "pytest-cov==6.0.0",
        "scipy==1.14.1",
        
        ],
    python_requires=">=3.8",  # Minimum Python version
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Or your chosen license
        "Operating System :: OS Independent",
        "Development Status ::  Alpha",  # Adjust status accordingly
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Intended Audience :: Developers",
    ],
    keywords="image-processing filters convolution transformations",
)
