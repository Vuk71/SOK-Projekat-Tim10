from setuptools import setup, find_packages

setup(
    name="load-github",
    version="0.1",
    packages=find_packages(),
    namespace_packages=['loader'],
    entry_points={
        'graph.load':
            ['load_github=loader.data_source_github:parse_data'],
    },
)
