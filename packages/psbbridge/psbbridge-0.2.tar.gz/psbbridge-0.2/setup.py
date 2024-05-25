from setuptools import setup, find_packages

def readme():
    with open('README.rst', 'r') as f:
        content = f.read()
    return content

setup(
    name='psbbridge',
    version='0.2',
    description='A Bridge for PacSpedd Base with IDE support',
    long_description=readme(),
    long_description_content_type='text/x-rst',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    author='PacSpedd',
    author_email='pacspedd@outlook.com',
    url='https://github.com/PacSpedd/psbbridge',
    license='MIT',
    install_requires=[
        'pacspeddbase',
        'maturin']
)
