from setuptools import setup, find_packages

setup(
    name="my_piglatin-translator",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    author="haruuuu003",
    author_email="s2222101@stu.musashino-u.ac.jp",
    description="A simple Pig Latin translator",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/haru0039633/my_piglatin-translator",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
