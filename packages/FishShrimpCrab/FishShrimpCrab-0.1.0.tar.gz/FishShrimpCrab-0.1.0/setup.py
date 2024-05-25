# setup.py

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="FishShrimpCrab",  # パッケージ名
    version="0.1.0",  # バージョン
    author="Li",  # 作者名
    description="A traditional HK game",  # 簡単な説明
    long_description=long_description,  # 長い説明（README.mdの内容）
    long_description_content_type="text/markdown",  # READMEの形式
    url="https://github.com/LiChinNgai/fishshrimpcrab",  # GitHubリポジトリのURL
    packages=find_packages(),  # パッケージの自動検出
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Pythonのバージョン要件
)
