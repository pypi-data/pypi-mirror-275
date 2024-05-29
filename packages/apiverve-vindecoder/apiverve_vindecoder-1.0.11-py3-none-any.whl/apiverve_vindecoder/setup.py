from setuptools import setup, find_packages

setup(
    name='apiverve_vindecoder',
    version='1.0.11',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests',
        'setuptools'
    ],
    description='VIN Decoder is a simple tool for decoding vehicle identification numbers. It returns the make, model, and more of the vehicle.',
    author='APIVerve',
    author_email='hello@apiverve.com',
    url='https://apiverve.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
