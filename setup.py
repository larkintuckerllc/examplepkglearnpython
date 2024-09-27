"""Configure distribution package."""
import setuptools


with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    author='John Tucker',
    author_email='john@larkintuckerllc.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    description='A small example package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    name='examplepkglearnpython',
    license="MIT",
    packages=setuptools.find_packages(),
    python_requires='>=3.12',
    url='https://github.com/larkintuckerllc/examplepkglearnpython',
    version='0.0.1',
)

