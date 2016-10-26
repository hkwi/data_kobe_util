About
=====
data_kobe_util is an utility for health checking https://data.city.kobe.lg.jp/
using CI(continuous integration) platform.

.. image:: https://travis-ci.org/hkwi/data_kobe_util.svg?branch=master
    :target: https://travis-ci.org/hkwi/data_kobe_util


License: Apache 2.0

hint.json
---------
`hint.json` は更新確認先のシードです。Array of Object になっています。
Object のキーは次のような意味になっています。

- a : Object の型を示します。Turtle/RDF における `rdf:type` が `a` であるココロです。

  - a=Crawl ウェブサイトにデータの一覧が掲載されているパターンです。
  - a=Html ウェブサイトの特定領域以下がデータ対象とされているパターンです。
  - a=Direct ウェブサイト掲載はないけれども、カタログサイトで掲載されているパターンです。

- index : Crawl の場合に使います。リソースの見出しになっているページです。
- re : a=Crawl の場合に使います。正規表現のパターンで、抽出したリンクに適用してデータを識別します。
- url : データの URL です。

