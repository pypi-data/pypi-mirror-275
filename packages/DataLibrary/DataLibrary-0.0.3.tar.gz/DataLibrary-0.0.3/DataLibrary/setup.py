from setuptools import setup,find_packages

setup(
    name = "DataLibrary",
    version = '0.0.3',
    packages= find_packages(),
    python_requires = '>=3.6',
    install_requires = [
        'pandas',
        'scikit-learn',
        'nltk',
        'numpy',
    ],
)