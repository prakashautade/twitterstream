import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="twitterstream",
    version="0.0.1",
    author="Prakash Autade",
    author_email="prakash.autade@gmail.com",
    description="Twitter stream consumer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/prakashautade/twitterstream",
    packages=setuptools.find_packages(),
    install_requires=[ 'tweepy', ]
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
