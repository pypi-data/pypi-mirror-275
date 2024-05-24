from setuptools import setup, find_packages

setup(
    name='memory_game',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'memory_game=memory_game.game:main',
        ],
    },
    description='A simple console-based memory game',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/memory_game',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

