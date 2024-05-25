from setuptools import setup

setup(
name='brainfuck-tool',
version='0.1.0',
author='omid',
author_email='omid377773@gmail.com',
description='This is the most complete "brainfuck" language tool',
packages=['brainfucktool'],
package_dir={'brainfucktool':'src/brainfucktool'},
classifiers=[
'Programming Language :: Python :: 3'
],
python_requires='>=3.8',
)
