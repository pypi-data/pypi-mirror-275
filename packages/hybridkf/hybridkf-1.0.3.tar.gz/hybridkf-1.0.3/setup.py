from setuptools import setup, find_packages

setup(
    name='hybridkf',
    version='1.0.3',
    packages=find_packages(),
    description='''An advanced implementation of the Kalman filter that handles and processes (pragmatic) continuous time-model state observations with discrete time-measurements for state estimation.'''
    ,
    author='akain0',
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib',
    ],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/akain0/hybridkf',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)