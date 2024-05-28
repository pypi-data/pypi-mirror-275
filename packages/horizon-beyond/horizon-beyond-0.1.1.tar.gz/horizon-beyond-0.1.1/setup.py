from setuptools import setup, find_packages

setup(
    name='horizon-beyond',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'horizon=horizon.module:hello_world',
        ],
    },
    url='https://github.com/msnabiel/horizon',
    license='MIT',
    author='Syed Nabiel Hasaan M',
    author_email='msyednabiel@gmail.com',
    description='A Python package with hip-hop and Gen Z-inspired function names for NumPy and TensorFlow operations.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)
