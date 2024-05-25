from setuptools import setup, find_packages

setup(
    name='hybridkf',
    version='1.0.0',
    packages=find_packages(),
    description='''An advanced implementation of the Kalman filter that handles and processes (pragmatic) continuous time-model state observations with discrete time-measurements for state estimation.'''
    ,
    author='akain0',
    url='https://github.com/yourusername/your-package-name',
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib',
        'random',
        'math'
    ],
)