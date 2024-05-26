from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    readme = "\n" + fh.read()

VERSION = '0.0.0'
DESCRIPTION = 'A library to port c++ to python.'

setup(
    name="vialin",
    version=VERSION,
    author="Schkimansky",
    author_email="<ahmadchawla1432@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=readme,
    packages=find_packages(),
    install_requires=[],
    keywords=['c++', 'python', 'python c++', 'port', 'porter', 'bind', 'binder', 'binding', 'bind c++'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
