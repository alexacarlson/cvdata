import setuptools, os

parent_dir = os.path.dirname(os.path.realpath(__file__))

with open(f"{parent_dir}/README.md", "r") as readme_file:
    long_description = readme_file.read()

setuptools.setup(
    name="cvdata",
    version="0.0.1",
    author="James Adams",
    author_email="monocongo@gmail.com",
    description="Tools for creating and manipulating computer vision datasets",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/monocongo/cvdata",
    packages=[
        "cvdata",
    ],
    provides=[
        "cvdata",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "boto3"
        "lxml"
        "numpy",
        "pandas",
        "pillow",
        "requests"
        "tqdm"
    ],
)