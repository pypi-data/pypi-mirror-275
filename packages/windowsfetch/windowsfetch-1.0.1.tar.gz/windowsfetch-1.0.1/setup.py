from setuptools import setup, find_packages

setup(
    name='windowsfetch',
    version='1.0.1',
    packages=find_packages(),
    description="command: winfetch. i made this as a funny windows version of neofetch in like an hour. do not expect this to be updated by me lol\nI ALSO BURNT THE NAME WINFETCH SO YOU HAVE TO INSTALL WITH WINDOWSFETCH NOW. RIP ME.",
    entry_points={
        'console_scripts': [
            'winfetch = winfetch.__main__:main',
        ],
    },
)
