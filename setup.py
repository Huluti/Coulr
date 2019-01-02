#!/usr/bin/env python3

from setuptools import setup, find_packages


setup(
    name='coulr',
    version='1.7',
    description='Enjoy colors and feel happy!',
    author='Hugo Posnic',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Topic :: Multimedia :: Graphics',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3 :: Only'
    ],
    keywords = 'colors colours coulr',
    packages=find_packages(),
    install_requires=['xdg'],
    include_package_data=True,
    data_files=[
        ('usr/share/pixmaps', ['coulr/assets/coulr.png']),
        ('usr/share/applications', ['coulr.desktop'])
    ],
    entry_points={
        'gui_scripts': [
            'coulr = coulr.main:main',
        ]
    }
)
