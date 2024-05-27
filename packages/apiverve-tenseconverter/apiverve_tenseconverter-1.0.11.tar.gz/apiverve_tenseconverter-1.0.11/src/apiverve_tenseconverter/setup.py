from setuptools import setup, find_packages

setup(
    name='apiverve_tenseconverter',
    version='1.0.11',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests',
        'setuptools'
    ],
    description='Tense Converter is a simple tool for converting text to past or future tense. It returns the text converted to the specified tense.',
    author='APIVerve',
    author_email='hello@apiverve.com',
    url='https://apiverve.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
