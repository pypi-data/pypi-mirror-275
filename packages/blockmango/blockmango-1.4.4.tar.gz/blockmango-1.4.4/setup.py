from setuptools import setup

setup(
    name='blockmango',
    version='1.4.4',
    packages=['blockmango'],
    install_requires=['requests'],
    author='Dark',
    author_email='darkness0777@proton.me',
    description='Blockman Go API package',
    url='https://github.com/darkkpy/blockmango',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
