from setuptools import setup, find_packages

setup(
    name='RDG-Networks',
    version='0.2.5',
    author='Niek Mooij',
    author_email='mooij.niek@gmail.com',
    description='Most of the code from the RDG Networks project',
    long_description=open('README.md').read(),
    url='https://github.com/NiekMooij/RDG_networks',
    classifiers=[
            'Programming Language :: Python :: 3',
            # 'License :: OSI Approved :: All Rights Reserved',
            'Operating System :: OS Independent'],
    license='All Rights Reserved',
    packages=find_packages(),
    install_requires=[
        'networkx',
        'numpy',
        'scipy',
        'shapely',
        'typing'
    ],
    entry_points={
        'console_scripts': [
            'generate_line_segments=RDG_networks.generate_line_segments:main',
            'generate_line_network=RDG_networks.generate_line_network:main',
            'get_intersection_segments=RDG_networks.get_intersection_segments:main',
            'generate_line_segments_dynamic=RDG_networks.generate_line_segments_dynamic:main',
            'draw_segments=RDG_networks.draw_segments:main'
        ],
    },
)