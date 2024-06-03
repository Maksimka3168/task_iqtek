from setuptools import setup, find_packages

with open('src/app/requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='iqtek_task',
    version='0.1.0',
    author='Makismka3168',
    author_email='gfer-6@mail.ru',
    packages=find_packages(where='src/app'),
    package_dir={'': 'src/app'},
    include_package_data=True,
    install_requires=required,
    entry_points={
        'console_scripts': [
            'iqtek_task = main:main',
        ],
    },
)