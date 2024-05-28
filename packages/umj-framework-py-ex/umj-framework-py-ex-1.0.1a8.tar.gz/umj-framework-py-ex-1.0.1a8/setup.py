from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='umj-framework-py-ex',
    version='1.0.1a8',
    author='Waffe-Wafle',
    description='A simple dinamic UI aiogram extension. Will be much more powered in future.',
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
    install_requires=[
        'aiogram>=3.5',
        'dill>=0.3.8',
        'dynamic_py_loader'
    ],
)
