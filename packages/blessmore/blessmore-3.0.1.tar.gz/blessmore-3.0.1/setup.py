from setuptools import setup, find_packages

setup(
    name="blessmore",
    version="3.0.1",  # Keep the same version number
    packages=find_packages(),
    install_requires=[
        "gensim",
        "huggingface_hub",
        "regex",
    ],
    description="A package to load Shona FastText embeddings,Train Fasttext Embedding and clean Shona text data",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/Blessmore2/blessmore",  # Replace with your GitHub repository URL
    author="Blessmore Majongwe",
    author_email="blessmoremajongwe@gmail.com",
    license="Apache 2.0",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9.12',
)
