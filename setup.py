from setuptools import setup

with open("README.rst", "r") as fd:
    long_description = fd.read()


setup(
    name='ordered-hash-set',
    version='0.1.1',
    description='Set that maintains insertion order',
    py_modules=['ordered_hash_set'],
    package_dir={'': 'src'},
    long_description=long_description,

    url="https://github.com/buyalsky/ordered-hash-set",
    author="Burak Dursunlar",
    author_email="burak.dursunlar@hotmail.com",

    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: Implementation :: CPython",
        "Operating System :: OS Independent",
    ]
)