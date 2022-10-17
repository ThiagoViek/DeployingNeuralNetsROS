from setuptools import setup
import os
from glob import glob

package_name = 'object-det-network'

setup(
    name=package_name,
    version='1.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='user',
    maintainer_email='thiago.viek@gmail.com',
    description='Deploying Neural Networks with GPU acceleration for Robots with ROS: A minimal example',
    license='MIT LICENSE',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'inferenceNode = object-det-network.inferenceNode:main',
            'imagePublisherNode = object-det-network.imagePublisherNode:main',
        ],
    },
)
