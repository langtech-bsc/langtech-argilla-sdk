from setuptools import setup, find_packages
import os

setup(
    name="galtea",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
        "argilla==2.3.0",
        "python-dotenv==1.0.1",
        "email-validator==2.1.2"
    ],
    description="...",
    long_description=open("README.md").read() if os.path.exists("README.md") else "",
    long_description_content_type="text/markdown",
    python_requires=">=3.6",
)