from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='clipboardhist',
    version='1.0.5',
    description='A simple tool for managing clipboard history.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='HIRO TAKAGI',
    author_email='s2222103@stu.musashino-u.ac.jp',
    url='https://github.com/h1l2o/clipboardhist',
    packages=find_packages(),
    install_requires=[
        'pyperclip',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
