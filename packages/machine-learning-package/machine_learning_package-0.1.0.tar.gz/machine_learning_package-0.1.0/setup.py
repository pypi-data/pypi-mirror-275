from setuptools import setup, find_packages

setup(
    name="machine_learning_package",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "matplotlib",
        "seaborn",
        "scikit-learn",
        "tensorflow",
        "keras"
    ],
    author="Jion",
    author_email="s2022042@stu.musasino-u.ac.jp",
    description="A package to import essential machine learning libraries",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/yourusername/machine_learning_package",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
