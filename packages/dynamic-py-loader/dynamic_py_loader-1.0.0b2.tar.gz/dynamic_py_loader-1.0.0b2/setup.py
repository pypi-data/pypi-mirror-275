from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='dynamic_py_loader',
    version='1.0.0b2',
    packages=find_packages(exclude=('tests')),
    author='Waffe-Wafle',
    description='A simple dynamic packages and modules loaders.',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/Waffe-Wafle/dynamic_py_loader',
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
