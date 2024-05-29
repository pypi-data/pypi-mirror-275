from setuptools import setup, find_packages

setup(
    name='apiverve_wordsextractor',
    version='1.0.11',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests',
        'setuptools'
    ],
    description='Word Extractor is a simple tool for extracting nouns, verbs, adjectives, adverbs, and more from text. It returns the extracted words based on the specified part of speech.',
    author='APIVerve',
    author_email='hello@apiverve.com',
    url='https://apiverve.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
