from setuptools import find_packages, setup

setup(
    name='bordersandpoints',
    packages=find_packages(include=['bordersandpoints']),
    version='1.0.0',
    install_requires=['numpy','opencv-python','matplotlib','Pillow','torch','torchvision','scikit-learn'],
    description='Library for finding border lines with point in 2D video',
    author='Malla Dhanraj',
)