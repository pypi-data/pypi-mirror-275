from setuptools import setup, find_packages

setup(
    name="CobwebIT",
    version="1.0.00",
    packages=find_packages(),
    include_package_data=True,
    description="This is a Complex of random things",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Francisek s",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.12',
)

# Make sure you have a README.md file in the same directory
