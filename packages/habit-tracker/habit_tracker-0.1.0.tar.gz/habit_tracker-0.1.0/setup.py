# setup.py

from setuptools import setup, find_packages

setup(
    name="habit_tracker",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "habits=habit_tracker.main:main",
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple habit tracker application",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/habit_tracker",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
