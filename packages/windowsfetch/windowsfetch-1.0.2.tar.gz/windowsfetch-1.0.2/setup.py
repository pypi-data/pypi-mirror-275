from setuptools import setup, find_packages

setup(
    name='windowsfetch',
    version='1.0.2',
    packages=find_packages(),
    author="gamerjamer43",
    author_email="gamerjamer43@protonmail.com",
    description="command: winfetch. i made this as a funny windows version of neofetch in like an hour. ",
    long_description="do not expect this to be updated by me lol\nI ALSO BURNT THE NAME WINFETCH SO YOU HAVE TO INSTALL WITH WINDOWSFETCH NOW. RIP ME.",
    license="GNU GENERAL PUBLIC LICENSE V3",
    platforms="windows",
    entry_points={
        'console_scripts': [
            'winfetch = winfetch.__main__:main',
        ],
    },
)
