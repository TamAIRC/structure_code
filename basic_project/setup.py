from setuptools import setup, find_packages
setup(
    name='your_project_name',
    version='0.1.0',
    packages=find_packages(exclude=['tests', 'docs']),
    include_package_data=True,
    install_requires=[
        # List the required libraries here
    ],
    entry_points={
        'console_scripts': [
            # Ex: 'your_command = your_module:main_function'
        ],
    },
)
