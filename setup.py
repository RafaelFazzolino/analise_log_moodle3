from setuptools import setup, find_packages

setup(
    name="chamadaunb",
    version='0.1',
    packages=['chamada'],
    install_requires=[
        'Click',
        'selenium==3.14.0',
    ],
    entry_points='''
        [console_scripts]
        chamadaunb=chamada.runner:start
    ''',
)
