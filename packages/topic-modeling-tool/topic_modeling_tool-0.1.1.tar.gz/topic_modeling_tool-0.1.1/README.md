# topic_modeling_tool

topic_modeling_toolは、テキストデータのトピックモデリングを行うためのシンプルなツールです。このパッケージを使用すると、与えられたテキストデータからトピックを抽出し、それらのトピックに関連する単語を表示することができます。

## 特徴

- テキストデータからトピックを抽出するための簡潔なインターフェース
- Latent Dirichlet Allocation（LDA）を使用したトピックモデリングのサポート
- ユーザーフレンドリーなトピック表示オプション

## インストール

パッケージをインストールするには、次のコマンドを実行します

```sh
pip install topic_modeling_tool
```

## サンプル
```sh
from topic_modeling_tool import TopicModeler

documents = [
    "I love programming in Python",
    "Python and Java are popular programming languages",
    "Machine learning and data science are exciting",
    "I enjoy learning new things in tech",
    "Artificial intelligence is the future"
]

modeler = TopicModeler(n_topics=2)
topic_distribution = modeler.fit_transform(documents)
modeler.print_topics(n_top_words=5)
```