from setuptools import setup
setup(
    name='YouTube',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'youtube=youtube:main'
        ]
    }
)