from setuptools import setup, find_packages

setup(
    name='DataFrameProcessor',  # Ensure this is a valid name
    version='1.0.1',  # Ensure this follows the proper versioning format
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[
        'pandas',
        'scikit-learn',
        'nltk',
        'numpy',
    ],
    # Add other metadata here as needed
)