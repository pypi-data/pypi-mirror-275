# PyPIの設定ファイル
# setup.pyを書く必要があるのは、importする際の環境構築を楽にするため + そのコードを用意するのが容易になるから
# 作り方はこちらのURLを見る
## https://qiita.com/Tadahiro_Yamamura/items/2cbcd272a96bb3761cc8

from setuptools import setup

setup(
    name="classification_tension_for_image",
    version="0.0.1",
    install_requires=["packageA", "packageB"],
    description="一言で書けるパッケージ概要",
    long_description="""
    複数行にわたるパッケージの詳細説明
    """,
    keywords="feeling, person face images, classification",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Communications :: Chat",
    ],
)

# install_requires: pip install -eで一緒にinstallされる
# entry_points: pip install したときに実行可能ファイルとして生成される
