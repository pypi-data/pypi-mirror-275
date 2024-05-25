from setuptools import setup, find_packages

setup(
    name='apiverve_distancecalculator',
    version='1.0.11',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests',
        'setuptools'
    ],
    description='Distance Calculator is a simple tool for calculating the distance between two locations. It returns the distance in miles and kilometers.',
    author='APIVerve',
    author_email='hello@apiverve.com',
    url='https://apiverve.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
