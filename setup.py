from setuptools import setup, find_packages
 
setup(
    name='clean_folder',
    version='0.1',
    description='Very useful code',
    author='Андрій',
    license='MIT',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'clean-folder = clean_folder.clean:main',
        ],
    }
)