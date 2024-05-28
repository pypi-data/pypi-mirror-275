from setuptools import setup, find_packages

setup(
    name="hashall",
    version="1.0.0",
    author="khiat Mohammed Abderrezzak",
    author_email="khiat.abderrezzak@gmail.com",
    license="MIT",
    description="Sophisticate Hashed Data Structures",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://pypi.org/project/hashall/",
    packages=find_packages(),
    install_requires=[
        "word2number>=1.1",
    ],
    keywords=[
        "hash",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.6",
)
