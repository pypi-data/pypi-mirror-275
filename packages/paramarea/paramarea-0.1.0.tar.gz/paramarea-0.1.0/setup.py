from setuptools import setup , find_packages

setup(
    name= "paramarea",
    packages=find_packages(  include=["paramarea"]   ),
    version="0.1.0",
    description="This library is capable of calculating area and circumference/perimeter of circle and rectangle. ",
    author="Girmada",
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)