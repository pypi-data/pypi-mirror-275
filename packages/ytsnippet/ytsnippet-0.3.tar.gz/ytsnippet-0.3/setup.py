from setuptools import setup, find_packages

setup(
    name='ytsnippet',
    version='0.3',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'ytsnippet=ytsnippet.cli:main',
        ],
    },
    install_requires=['prompt_toolkit'],
    author='Your Name',
    author_email='s2222038@stu.musashino-u.ac.jp',
    description='A simple code snippet manager',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/ytsnippet',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
