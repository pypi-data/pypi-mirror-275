# setup.py
from setuptools import setup, find_packages

setup(
    name="url_scheduler",
    version="0.1.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "url_scheduler=url_scheduler.scheduler:main",
        ],
    },
    author="2222041",
    author_email="s2222041@stu.musashino-u.ac.jp",
    description="A URL scheduler for managing weekly tasks.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/2222041/test.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

