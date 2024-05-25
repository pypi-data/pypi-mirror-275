from setuptools import setup, find_packages

setup(
    name='subfinder-leakix', 
    version='1.1.2',
    packages=find_packages(),  
    author='Jhonson12',
    author_email='wannaajhonson@gmail.com',
    url='https://github.com/Jhonsonwannaa/subfinder-by-leakix', 
    install_requires=[  
        'requests','rich',  
    ],
    
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown'
)
