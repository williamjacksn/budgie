from setuptools import find_packages, setup

setup(
    name='budgie',
    version='1.0.0',
    author='William Jackson',
    author_email='william@subtlecoolness.com',
    packages=find_packages(),
    install_requires=['Flask'],
    entry_points={
        'console_scripts': [
            'budgie = budgie.budgie:main'
        ]
    }
)
