# setup.py
from setuptools import setup, find_packages

setup(
    name='timetrace',
    packages=['timetrace'],
    
    version='0.2.2',
    
    license='MIT',
    
    install_requires=['matplotlib'],
    
    author='namake',
    author_email='s2222102@stu.musashino-u.ac.jp',
    
    description='A simple performance tracing and visualization library for Python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    
    # url='https://github.com/GamouYugo/timetrace',
    
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
