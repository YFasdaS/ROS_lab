from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'jekessova_duvanov_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'),
        glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='i-mv',
    maintainer_email='i-mv@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'even_publisher = jekessova_duvanov_pkg.even_number_publisher:main',
            'overflow_listener = jekessova_duvanov_pkg.overflow_listener:main',
            'listener = jekessova_duvanov_pkg.listener:main',
            'talker = jekessova_duvanov_pkg.talker:main',
            'first_node = jekessova_duvanov_pkg.first_node:main',
            'time_printer = jekessova_duvanov_pkg.time_printer:main',
        ],
    },
)
