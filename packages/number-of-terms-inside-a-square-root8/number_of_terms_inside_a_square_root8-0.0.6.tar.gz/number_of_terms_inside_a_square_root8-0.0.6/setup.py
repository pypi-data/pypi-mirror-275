import setuptools
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="number-of-terms-inside-a-square-root8",
    version="0.0.6",  # バージョンを更新
    packages=find_packages(),
    author="yuki shimizu",
    author_email="s2222106@stu.musashino-u.ac.jp",
    description="Application to Determine the Number of Terms Inside a Square Root",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gomaW/suuzikadai4.git",
    project_urls={
        "Bug Tracker": "https://github.com/gomaW/suuzikadai4/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    py_modules=["keisannkadai1"],  # モジュール名を修正
    python_requires=">=3.8",
    entry_points={
        'console_scripts': [
            'number-of-terms-inside-a-square-root = keisannkadai1:main'  # 正しいモジュールと関数名を指定
        ]
    },
)
