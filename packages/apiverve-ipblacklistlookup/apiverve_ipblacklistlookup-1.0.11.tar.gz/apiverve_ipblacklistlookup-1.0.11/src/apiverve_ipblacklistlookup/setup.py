from setuptools import setup, find_packages

setup(
    name='apiverve_ipblacklistlookup',
    version='1.0.11',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests',
        'setuptools'
    ],
    description='IP Blacklist Lookup is a simple tool for looking up if an IP address is in a blacklist. It returns the blacklist name and the reason for the blacklist.',
    author='APIVerve',
    author_email='hello@apiverve.com',
    url='https://apiverve.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
