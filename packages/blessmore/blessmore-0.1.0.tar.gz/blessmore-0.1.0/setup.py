from setuptools import setup, find_packages

setup(
    name="blessmore",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "gensim",
        "huggingface_hub",
    ],
    description="A package to load Shona FastText embeddings from Hugging Face",
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
    python_requires='>=3.6',
)
