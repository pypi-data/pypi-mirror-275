from setuptools import setup, find_packages

setup(
    name="Calulator2",
    version="0.3",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'Calculator = Calculator:main',
        ],
    },
)