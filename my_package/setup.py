from setuptools import find_packages, setup

package_name = 'my_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='dell',
    maintainer_email='ishabhatp@gmil.com',
    description='Beginner client libraries tutorials practice package',
    license='Apache License 2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
        'my_node = my_package.my_node:main',
	'taskone_publisher = my_package.taskone_publisher:main',
	 'taskone_subscriber = my_package.taskone_subscriber:main',
        ],
    },
)
