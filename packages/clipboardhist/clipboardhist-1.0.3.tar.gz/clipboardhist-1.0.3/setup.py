from setuptools import setup, find_packages

setup(
    name='clipboardhist',
    version='1.0.3',
    description='A simple clipboard history management tool',
    author='HIRO TAKAGI',
    author_email='s2222103@stu.musashino-u.ac.jp',
    url='https://github.com/h1l2o/clipboardhist.git',
    packages=find_packages(),
    install_requires=['pyperclip'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
