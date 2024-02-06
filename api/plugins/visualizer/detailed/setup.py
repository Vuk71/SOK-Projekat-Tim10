from setuptools import setup, find_packages

setup(
    name="detailed_visualizer",
    version="0.1",
    packages=find_packages(),
    install_requires=['Core >= 0.1'],
    namespace_packages=['visualizer'],
    package_data={'visualizer': ['detailed_main_view.js']},
    entry_points={
        'visualizer':
            ['detailed_visualizer=visualizer.detailed_visualizer:DetailedVisualizer']
    }
)