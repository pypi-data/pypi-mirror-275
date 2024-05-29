from setuptools import setup, find_packages

setup(
    name="dicio-py",
    version="2.5",
    author="Jeiel Lima Miranda",
    description="Script para buscar o significado de palavras no dicionário online Dicio.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/Jetrom17/dicio-py",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'dicio-py=dicio_py.dicio_py:main',
        ],
    },
)
