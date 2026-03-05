import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

version = "0.0.1"

REPO_NAME = "TextSummarizer"
AUTHOR_USER_NAME = "Nikhil Kaushik"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "nikhilkaushik171@gmail.com"

# this is the setup code - it will look for constructor file in every folder
# and will install this as a local package

setuptools.setup(
name=SRC_REPO,
version=version,
author="Nikhil Kaushik",
author_email="nikhilkaushik171@gmail.com",
description="Abstractive Text Summarization using PEGASUS and HuggingFace Transformers",
long_description=long_description,
long_description_content_type="text/markdown",
url=f"https://github.com/Nikhilkaushik7/TextSummarizer",
project_urls={
"Bug Tracker": f"https://github.com/Nikhilkaushik7/TextSummarizer/issues",
},
package_dir={"": "src"},
packages=setuptools.find_packages(where="src"),
python_requires=">=3.8",
)