import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="testwizard.commands-video",
    version="3.8.0",
    author="Resillion - Belgium",
    author_email="testwizard-support@resillion.com",
    description="Testwizard Video commands",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.resillion.com/testwizard/",
    packages=['testwizard.commands_video'],
    install_requires=[
        'testwizard.commands-core==3.8.0'
    ],
    classifiers=[
        "Programming Language :: Python :: 3.3",
        "Development Status :: 5 - Production/Stable",
        "Operating System :: OS Independent",
    ],
)













