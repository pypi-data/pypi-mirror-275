from setuptools import setup, find_packages

setup(
    name='eth_mnemonic_to_key',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'eth-account',
        'requests',
        'cryptography',
    ],
)