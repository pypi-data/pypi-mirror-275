from setuptools import setup

setup(
    name='pyNovelist',
    version='0.1.0',
    author='David Condrey',
    author_email='davidcondrey@protonmail.com',
    description='Comprehensive tool designed to assist in generating and refining novel content.e',
    packages=['pynovelist'],
    install_requires=[
        'openai',
        'nltk',
	'scikit-learn',
	'pandas',
	'spacy',
	'transformers'
    ],
)
