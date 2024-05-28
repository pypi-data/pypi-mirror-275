from setuptools import setup, find_packages

setup(
    name='NameExtractor',
    version='1.0.4',
    packages=find_packages('src', exclude=['tests']),
    package_dir={'': 'src'},
    author="Defying Gravity",
    description="Name Extractor is a small AI program to extract name and gender from characters in text.",
    long_description=open("README.md", "r").read(),
    long_description_content_type='text/markdown',
    url='https://github.com/xDefyingGravity/Name-Extractor/',
    install_requires=[
        "nltk",
        "spacy"
    ],
    dependency_links=[
        "https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.1.0/en_core_web_sm-3.1.0.tar.gz#egg=en_core_web_sm",
    ],
)
