from setuptools import setup, find_packages

# use python setup.py sdist bdist_wheel to build
# then twine upload dist/* to upload to PyPi (note, include the prepend pypi-...apikey

VERSION = "0.0.3"
DESCRIPTION = "Common tools for historians to aid text analysis."
LONG_DESCRIPTION = "Common tools for historians to parse text more easily before feeding the text into larger text analysis pipelines."

setup(
    name="historianstexttools",
    version=VERSION,
    author="Christopher Thomas Goodwin",
    author_email="<ctg7w6@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    readme="README.md",
    packages=find_packages(),
    install_requires=["nltk>=3.8.1",
                      "spacy>=3.7.4"],

    keywords=['python', 'historian', 'text', 'text-analysis'],
    classifiers=["Development Status :: 3 - Alpha",
                 "Intended Audience :: Science/Research",
                 "License :: OSI Approved :: MIT License",
                 "Operating System :: OS Independent"
    ]
)