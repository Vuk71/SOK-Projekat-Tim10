from setuptools import setup, find_packages

setup(
    name="core",
    version="0.1",
    packages=find_packages(),
    namespace_packages=['core'],
    provides=['core.services', 'models'],
    zip_safe=True
)
