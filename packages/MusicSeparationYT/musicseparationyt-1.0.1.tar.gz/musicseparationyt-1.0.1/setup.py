#!/usr/bin/env python3

# from setuptools import setup, find_packages
import setuptools
# from setuptools import find_packages

# パッケージの基本情報
name = "MusicSeparationYT"  # パッケージ名
version = "1.0.1"  # バージョン番号
description = "this tool music download and seprate"  # パッケージの説明
long_description_content_type="text/markdown",
author = "Y-Ryohei"  # 作者名
author_email = ""  # 作者のメールアドレス
url = "https://github.com/Y-Ryohei/MusicSeparationYT"  # リポジトリURL
license = "MIT"  # ライセンス

# インストールに必要な依存関係
requirements = [
  'pytube==15.0.0',
  'moviepy==1.0.3',
  'demucs==4.0.3',
]

# パッケージに含めるモジュール
# packages = find_packages(),

# その他の情報
classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.6",
    "Topic :: Software Development :: Libraries",
]

# セットアップ処理
setuptools.setup(
    name=name,
    version=version,
    description=description,
    author=author,
    author_email=author_email,
    url=url,
    license=license,
    install_requires=requirements,
    # packages=packages,
    classifiers=classifiers,
)
