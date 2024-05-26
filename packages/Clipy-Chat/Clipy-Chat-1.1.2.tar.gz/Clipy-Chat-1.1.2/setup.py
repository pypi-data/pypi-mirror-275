# setup.py

from setuptools import setup, find_packages

setup(
    name='Clipy-Chat',
    version='1.1.2',
    packages=find_packages(),
   entry_points={
        'console_scripts': [
            'clipy-chat=clipy_chat.cli:main',
        ],
    },
    install_requires=[],
    author='Santosh Giri',
    author_email='santoshgiri2345@gmail.com',
    description='A simple CLI based chat',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/santosh2345/clipy-chat',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
