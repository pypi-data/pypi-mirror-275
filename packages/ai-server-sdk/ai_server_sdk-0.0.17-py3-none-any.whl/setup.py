from setuptools import find_packages, setup

with open('README.md','r') as f:
    long_description = f.read()
    
setup(
    name="ai-server-sdk",                     # This is the name of the package
    version="0.0.17",
    packages=find_packages(),
    install_requires=[
        'requests', 
        'pandas', 
        'jsonpickle',
    ], 
    extras_require={
        "full": ["langchain", "langchain-community"]
    },
    author="Thomas Trankle, Maher Khalil, Ryan Weiler",
    description="Utility package to connect to AI Server instances.",
    license="MIT",
    long_description = long_description,
    long_description_content_type = 'text/markdown'
)