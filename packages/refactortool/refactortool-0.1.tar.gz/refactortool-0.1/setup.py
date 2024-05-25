# setup.py
from setuptools import setup, find_packages

setup(
    name='refactortool',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'autopep8',
        'pylint',
        'black',
        'isort',
        'flake8',
        'pytest',
    ],
    entry_points={
        'console_scripts': [
            'refactortool=refactortool:main',
        ],
    },
    author="Yuna Suzuki",
    author_email="s2222077@stu.musashino-u.ac.jp",
    description="A tool for improving code quality by analyzing and refactoring project code.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yuna-musashino/refactortool",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
