from setuptools import setup, find_packages

setup(
    name="load json",
    version="0.1",
    packages=find_packages(),
    namespace_packages=['loader'],
    entry_points={
        'graph.load':
            ['load_json=loader.data_source_json_file:FileSystemJSONPlugin'],
    },
)
