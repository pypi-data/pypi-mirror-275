import sys
import subprocess
from setuptools import setup
from setuptools.command.install import install

setup(
    name='RadeonMaster',  
    version='0.1.1', 
    author='Vigneswaran S',  
    author_email='contactmevigneswaran@gmail.com',  
    description='Radeon monitor for python', 
    long_description=open('README.md').read(), 
    long_description_content_type='text/markdown', 
    url='https://github.com/MegalosVigneswaran/RadeonMaster',   
    classifiers=[
        'Programming Language :: Python :: 3',  
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
    ],
    keywords='radeon gpu amd monitor linux radeontop',
    python_requires='>=3.6',
    py_modules=['RadeonMaster']
)
