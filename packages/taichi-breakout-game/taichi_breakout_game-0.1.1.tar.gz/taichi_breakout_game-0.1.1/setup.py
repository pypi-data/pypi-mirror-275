# setup.py

from setuptools import setup, find_packages

setup(
    name="taichi_breakout_game",
    version="0.1.1",
    packages=find_packages(),
    install_requires=["pygame"],
    entry_points={
        "console_scripts": [
            "breakout_game=breakout_game.game:main",
        ],
    },
    author="Taichi Fujiki",
    author_email="s2222071@stu.musashino-u.ac.jp",
    description="A simple Breakout game implemented in Python using Pygame",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https:/Fujiki-Taichi/github.com//breakout_game",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
