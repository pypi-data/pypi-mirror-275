from setuptools import setup, find_packages

setup(
    name="parupome",  # パッケージ名
    version="0.1",  # バージョン番号
    author="sugiyama",  # 作者名
    author_email="s2222050@stu.musashino-u.ac.jp",  # 作者のメールアドレス
    description="A simple package to convert datetime between timezones",  # パッケージの簡単な説明
    long_description=open('README.md').read(),  # パッケージの詳細な説明（README.mdから読み込み）
    long_description_content_type="text/markdown",  # long_descriptionのフォーマット
    url="https://github.com/yourusername/parupome",  # パッケージのホームページのURL
    packages=find_packages(),  # パッケージの自動検索
    install_requires=[
        'pytz',  # 依存パッケージ
    ],
    classifiers=[
        "Programming Language :: Python :: 3",  # Pythonのバージョン
        "License :: OSI Approved :: MIT License",  # ライセンス
        "Operating System :: OS Independent",  # OSに依存しない
    ],
    python_requires='>=3.7',  # Pythonの最低バージョン
)
