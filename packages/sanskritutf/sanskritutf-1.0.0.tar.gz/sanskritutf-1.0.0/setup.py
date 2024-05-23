from setuptools import find_packages, setup

setup(
    name='sanskritutf',
    packages=find_packages(),
    version='0.1.0',
    description='Sanskrit UTF conversion library',
    author='Ashok Kumar',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==8.2.1'],
    test_suite='tests',
)
