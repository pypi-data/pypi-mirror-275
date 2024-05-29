from pathlib import Path
from setuptools import setup, find_packages

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(name='animatedledstrip-client',
      version='1.1.0',
      url='https://github.com/AnimatedLEDStrip/client-python',
      license='MIT',
      author='Max Narvaez',
      author_email='mnmax.narvaez3@gmail.com',
      description='Library for communicating with an AnimatedLEDStrip server',
      long_description=long_description,
      long_description_content_type='text/markdown',
      packages=find_packages())
