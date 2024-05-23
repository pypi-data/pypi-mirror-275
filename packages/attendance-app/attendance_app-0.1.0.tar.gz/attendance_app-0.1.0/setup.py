from setuptools import setup, find_packages

setup(
    name='attendance_app',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask',
    ],
    entry_points={
        'console_scripts': [
        'your_script_name=attendance_app.app:main',
        ],
    },
)
