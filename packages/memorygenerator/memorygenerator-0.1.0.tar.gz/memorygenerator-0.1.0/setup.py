# setup.py
from setuptools import setup, find_packages

setup(
    name='memorygenerator',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'memory-generator=memorygenerator.__main__:main',
        ],
    },
    author="Yuna Suzuki",
    author_email="s2222077@stu.musashino-u.ac.jp",
    description="A tool for improving code quality by analyzing and refactoring project code.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yuna-musashino/refactortool",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
