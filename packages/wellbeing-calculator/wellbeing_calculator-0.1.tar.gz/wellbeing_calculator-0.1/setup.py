from setuptools import setup, find_packages

setup(
    name='wellbeing_calculator',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'pandas',
    ],
    entry_points={
        'console_scripts': [
            'wellbeing_calculator=wellbeing_calculator.calculator:main',
        ],
    },
)
