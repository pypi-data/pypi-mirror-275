from setuptools import setup, find_packages

setup(
    name='TextToVector',
    version='0.1.1',
    author='Eugene Evstafev',
    author_email='ee345@cam.ac.uk',
    description='A package to convert text into embedding vectors using Hugging Face models.',
    packages=find_packages(),
    install_requires=[
        'transformers>=4.0.0',
        'torch>=1.7.1'
    ],
    python_requires='>=3.6',
)
