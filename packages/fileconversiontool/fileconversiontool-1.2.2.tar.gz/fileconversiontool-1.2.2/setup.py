from setuptools import setup, find_packages

setup(
    name='fileconversiontool',
    version='1.2.2',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib',
        'pydicom',
        'SimpleITK',
        'opencv-contrib-python',
        'tqdm',
        'colorama',
        'nibabel'
    ],
    entry_points={
        'console_scripts': [
            'fileconversiontool = FileConversionTool.cli:main'
        ],
    },
    author='Wei-Chun Kevin Tsai',
    author_email='coachweichun@gmail.com',
    description='A Python package for converting medical imaging files between different formats.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='All Rights Reserved',
)
