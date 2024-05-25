from setuptools import setup, find_packages

setup(
    name="data_cleaning_assistant",
    version="0.1.0",
    author="Komo Takizawa",
    author_email="s2222078@stu.musashino-u.ac.jp",
    description="A comprehensive data cleaning assistant for pandas DataFrames.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/komo-tento/data_cleaning_assistant.git",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "pandas",
        "matplotlib",
        "seaborn",
        "scikit-learn"
    ],
    test_suite='tests',
)
