from setuptools import setup, find_packages

setup(
    name="visualize basic graph",
    version="0.1",
    packages=find_packages(),
    namespace_packages=['visualizer'],
    # Grupa za prikazivanje fakulteta
    # `prikaz_obican` je alias za rs.uns.ftn.fakultet.prikaz_obican:FakultetPrikazObican
    entry_points={
        'graph.visualizer':
            ['visualize_basic=visualizer.basic_visualizer:VisualizeBasic'],
    },
)
