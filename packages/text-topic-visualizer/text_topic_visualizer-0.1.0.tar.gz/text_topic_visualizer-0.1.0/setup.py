# setup.py

from setuptools import setup, find_packages

setup(
    name="text_topic_visualizer",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "gensim",
        "nltk",
        "pyLDAvis"
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A package for extracting and visualizing topics from text data",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/text_topic_visualizer",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
