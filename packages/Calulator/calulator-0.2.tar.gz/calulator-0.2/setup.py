from setuptools import setup, find_packages

setup(
    name="Calulator",
    version="0.2",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'Calculator = Calculator:main',
        ],
    },
)