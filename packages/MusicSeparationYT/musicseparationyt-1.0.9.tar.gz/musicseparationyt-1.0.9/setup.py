#!/usr/bin/env python3

from setuptools import setup, find_packages
import os
import setuptools
from setuptools import find_packages

# current_directory = os.path.abspath(os.path.dirname(__file__))

# READMEファイルを読み込む関数
# def read_readme():
#     with open(os.path.join(current_directory, 'README.md'), encoding='utf-8') as f:
#         return f.read()


# パッケージの基本情報
name = "MusicSeparationYT"  # パッケージ名
version = "1.0.7"  # バージョン番号
description = "this tool music download and seprate"  # パッケージの説明

# long_description=read_readme(),  
long_description=open('README.md').read(),
long_description_content_type='text/markdown',  

# long_description_content_type="text/markdown"
# long_description = "README.md"  # 詳細な説明
author = "Y-Ryohei"  # 作者名
# author_email = ""  # 作者のメールアドレス
# url = "https://github.com/Y-Ryohei/MusicSeparationYT"  # リポジトリURL
license = "MIT"  # ライセンス

# インストールに必要な依存関係
requirements = [
  'pytube',
  'moviepy',
  'demucs',
]

# パッケージに含めるモジュール
packages = find_packages()

# その他の情報
classifiers = [
    # "Development Status :: 4 - Beta",
    # "Intended Audience :: Developers",
    # "License :: OSI Approved :: MIT License",
    # "Programming Language :: Python :: 3.6",
    # "Topic :: Software Development :: Libraries",
]

# # セットアップ処理
# setuptools.setup(
#     name=name,
#     version=version,
#     description=description,
#     long_description=long_description,
#     long_description_content_type=long_description_content_type,
#     author=author,
#     # author_email=author_email,
#     # url=url,
#     license=license,
#     install_requires=requirements,
#     packages=packages,
#     classifiers=classifiers,
# )

setuptools.setup(
  # パッケージの基本情報
  name = "MusicSeparationYT",  # パッケージ名
  version = "1.0.9",  # バージョン番号
  description = "this tool music download and seprate",  # パッケージの説明
  
  # 詳細な説明
  # long_description=read_readme(),
  long_description=open('README.md').read(),
  long_description_content_type='text/markdown',  
  
  author = "Y-Ryohei",  # 作者名
  license = "MIT",  # ライセンス
  
  # インストールに必要な依存関係
  requirements = [
    'pytube',
    'moviepy',
    'demucs',
  ],
  
  # パッケージに含めるモジュール
  packages = find_packages(),
)