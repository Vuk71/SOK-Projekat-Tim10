from setuptools import setup, find_packages

setup(
    name="load instagram",
    version="0.1",
    packages=find_packages(),
    namespace_packages=['loader'],
    entry_points={
        'graph.load':
            ['load_instagram=loader.data_source_instagram:DataSourceInstagram'],
    },
)
