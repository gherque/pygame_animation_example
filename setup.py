from setuptools import setup

setup(
    name="movement",
    version="0.0.1",
    packages=["movement"],
    entry_points={
        "console_scripts": [
            "movement = movement.__main__:main"
        ]
    },
)