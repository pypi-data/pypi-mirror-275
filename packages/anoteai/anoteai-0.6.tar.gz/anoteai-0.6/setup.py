from setuptools import setup, find_packages

setup(
    name='anoteai',
    version='0.6',
    packages=find_packages(),
    install_requires=['requests'],
    description='An SDK for interacting with the Anote API',
    author='Natan Vidra',
    author_email='nvidra@anote.ai',
    url='https://github.com/nv78/Anote',
    license='MIT',
)