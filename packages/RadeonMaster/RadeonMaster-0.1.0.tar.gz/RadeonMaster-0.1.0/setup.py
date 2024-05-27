import sys
import subprocess
from setuptools import setup

def check_dependencies():

    message = """
These packages are not available.

Please install these packages by your package manager."""
    error = False
    if subprocess.getoutput("command -v radeontop") == '':
        error = True
        "*radeontop"+message
    if subprocess.getoutput("command -v sensors") == '':
        error = True
        "*lm-sensors"+message  
    if error == True:
        raise RuntimeError(message)

def check_platform():
    if not sys.platform.startswith("linux"):
        raise RuntimeError("This package can only be installed on Linux.")

check_platform()
check_dependencies()

setup(
    name='RadeonMaster',  
    version='0.1.0', 
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
