# 概要

nanika は、複数の音声ファイルを一括で処理し、csv ファイルに MFCC 特徴量を記録できるツールです.
librosa で動く音声ファイルであれば動きます。

# 機能

- 複数のファイルをまとめて抽出、記録する
- 変換前のファイルはすべて残ります

## インストール

```
pip3 install nanika
```

## 使い方 example

- ライブラリのインポート

```
import nanika as nk
```

- 処理の設定
- extension = "拡張子の指定"
- folder_path = "特徴量を抽出したい音声ファイルのフォルダの指定"
- output_csv = "抽出後の csv ファイル保存場所の指定"

- プログラム例

```
# フォルダパスを設定
extension = "mp3"
folder_path = "/Users/sugawara/dstokuron/src/music"
output_csv = "/Users/sugawara/dstokuron/src/res/audio_v2.csv"

# 変換処理を実行
nk.extract_mfcc_features(folder_path, output_csv, extension)
```

# 変換後の注意

- 入力フォルダが存在していることを確認してください
- フォルダ内に変換するファイルが存在していることを確認してください。
- 出力フォルダが存在していることを確認してください。

# サポート

バグ報告や機能リクエストはメールにてご連絡ください。

# ライセンス

このプログラムは [MIT License](https://choosealicense.com/licenses/mit/) でライセンスされています。

## バージョン

0.1.1
