from setuptools import setup, find_packages

setup(
    name='apiverve_counter',
    version='1.0.9',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests',
        'setuptools'
    ],
    description='Counter is a simple tool for incrementing, decrementing, and resetting a counter. It returns the current value of the counter.',
    author='APIVerve',
    author_email='hello@apiverve.com',
    url='https://apiverve.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
