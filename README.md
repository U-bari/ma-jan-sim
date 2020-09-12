# Name
Mahjong-simulator
Mリーグの対局をシミュレートします

# DEMO
![demo](https://user-images.githubusercontent.com/70689368/92993921-c45ebd80-f530-11ea-8ba6-e4dba977babf.png)

# Features

対局の確率計算に用いるレーティングはElo　ratingを改造し4人対戦型の競技でも使用できるようにしたものを使っています。
レートの推移もグラフで確認できます。

# Requirement

* python 3.8
* matplotlib

# Usage

DEMOの実行方法など、"hoge"の基本的な使い方を説明する

expect_app.pyを実行します。
![usage](https://user-images.githubusercontent.com/70689368/92993955-0556d200-f531-11ea-9c4d-479b54506149.png)
そうすると上のような画面が立ち上がります。係数指定にはデフォルト値の使用を勧めます（のちに詳しく解説します）。
選手名を選び入力し、okボタンを押すと選択した4人の選手の対局結果の予想と、レートの推移を表示します。

# Note

expect_app.pyが本体です。GUIを表示するためのコードが書かれています。
dateファイルには過去のMリーグの対局データが入っており、data.pyは対局データを読み込んでいます。
rate_system.pyではレート計算に用いる関数を幾つか定義しています。
M_rate.pyはコマンドプロンプト上で対局の予想を入出力するものです。expect_app.pyに手を加えたのちに実行結果が正しいかこちらと確認するのに使います。

レート計算方法についてはこちらに記しました。
[レート計算方法.pdf](https://github.com/U-bari/ma-jan-sim/files/5212560/untitled-1.pdf)
