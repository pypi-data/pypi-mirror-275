import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="dicio-py",
  version="2.2",
  author="Jetrom17",
  author_email="Jeiel@duck.com",
  description="Dicionário via CLI",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/Jetrom17/dicio-py",
  packages=setuptools.find_packages(),
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Operating System :: OS Independent",
  ],
  python_requires='>=3.0',
  entry_points={
      'console_scripts': [
          'dicio.py = dicio:main'
      ]
  }
)
