try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='map_boxes',
    version='1.0.6',
    author='Roman Sol (ZFTurbo)',
    packages=['map_boxes'],
    url='https://github.com/ZFTurbo/Mean-Average-Precision-for-Boxes',
    description='Function to calculate mean average precision (mAP) for set of boxes.',
    long_description='Function to calculate mean average precision (mAP) for set of boxes. Useful for object detection pipelines.',
)
