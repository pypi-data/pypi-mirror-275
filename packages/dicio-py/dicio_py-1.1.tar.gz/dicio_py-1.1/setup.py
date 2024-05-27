import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dicio-py",  # Replace with your own username
    version="1.1",
    author="Jetrom17",
    author_email="Jeiel@duck.com",
    description="Dicionário via CLI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Jetrom17/dicio-py",
    packages=setuptools.find_packages(),
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'dicio-py=dicio_py:main',
        ],
    },
    python_requires='>=3.0',
)
