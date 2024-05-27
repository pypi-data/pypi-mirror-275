from setuptools import setup

setup(
    name='apimyllama',
    version='1.0.0',
    description='A package for interacting with the APIMyLlama API',
    author='Liam Vang',
    author_email='gimerstudios@gmail.com',
    py_modules=['apimyllama'],
    install_requires=['requests'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
