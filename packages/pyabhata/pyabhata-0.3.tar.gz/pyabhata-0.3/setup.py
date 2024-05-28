from setuptools import setup, find_packages

setup(
    name='pyabhata',
    version='0.3',
    packages=find_packages(),
    install_requires=[
        'python-math',
    ],
    description='A mathematical library honoring Aryabhata',
    author='TheYellowAstronaut',
    author_email='malli.advait0@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
