# PyPIの設定ファイル
# setup.pyを書く必要があるのは、importする際の環境構築を楽にするため + そのコードを用意するのが容易になるから
# 作り方はこちらのURLを見る
## https://qiita.com/Tadahiro_Yamamura/items/2cbcd272a96bb3761cc8

from setuptools import setup

setup(
    name="classification_tension_for_image",
    version="0.0.3",
    install_requires=["packageA", "packageB"],
    description="""
    ユーザの顔写真からユーザのテンションを7段階に分類するモデル
    Model that classifies user tension into seven levels based on their facial photo

    """,
    long_description="""
    このモデルは、ユーザーの顔画像からユーザのテンションを7段階に分類する。このモデルは、ResNet152をベースにしたモデルで、学習済みの重みを用いている。このモデルは、PyTorchを用いて実装されている。
    入力：画像のパス
    出力：ユーザのテンションを7段階に分類した結果の上位2つのクラスとその確率(これについて変更したい場合は、img_classificationのnum_candidatesを変更してください)

    モデルの詳細については以下のリンクを参照してください。(日本語です。)
    https://docs.google.com/presentation/d/1GaxtnU9zE2ymMLbLYAQpq1QF3LJJaoo1cY_HZUNi_vc/edit?usp=sharing 

    This model classifies user tension into seven levels based on their facial images. It is based on the ResNet152 model and utilizes pretrained weights. The model is implemented using PyTorch.
    Input: Path to the image
    Output: Top two classes of user tension levels and their probabilities (to modify this, please change the num_candidates in img_classification)

    For more details about the model, please refer to the following link (content is in Japanese).
    https://docs.google.com/presentation/d/1GaxtnU9zE2ymMLbLYAQpq1QF3LJJaoo1cY_HZUNi_vc/edit?usp=sharing

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
