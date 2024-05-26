from setuptools import setup, find_packages


VERSION = '0.0.7'

setup(
    name='neginver',
    version=VERSION,
    author='flemyng feng',
    author_email='flemyng1999@outlook.com',
    description='A Python project for automatic Negative Film inversion',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    keywords=['python', 'negative', 'film', 'windows', 'mac', 'linux'],
    url='https://github.com/Flemyng1999/neginver',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
    install_requires=[
        'numpy',
        'scipy',
        'tqdm',
        'tifffile',
        'scikit-image',
        'matplotlib',
    ],
)
