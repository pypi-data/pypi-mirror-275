from setuptools import setup, find_packages

setup(
    name='oslab',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    include_package_data=True,
    package_data={
        'oslab': ['files/*.txt', 'files/*.py']
    },
)
