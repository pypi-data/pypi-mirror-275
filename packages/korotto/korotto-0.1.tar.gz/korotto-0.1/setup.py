from setuptools import setup, find_packages

setup(
    name="korotto",
    version="0.1",
    author="saito_haruto",
    author_email="s2222016@stu.musashino-u.ac.jp",
    description="A simple package to generate secure passwords",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/harutosaisai/korotto",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)