# setup.py
from setuptools import setup, find_packages
import pathlib
here = pathlib.Path(__file__).parent
long_description = (here / "README.md").read_text(encoding="utf-8")
setup(
    name='pyperclip_plus',
    version='0.1.9',
    packages=find_packages(),
    description='An enhanced clipboard management tool',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/pyperclip_plus',  # プロジェクトのURLを設定
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
    "pyperclip>=1.8.2"
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
