from setuptools import setup, find_packages

# Read the contents of your README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='ai_games',
    version='0.1.6',
    author='Coding with BM',
    description='AI Games: Collection of interactive games with AI opponents for Python.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/bzm10/ai_games',
    packages=find_packages(),
    install_requires=[
        'pygame'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
