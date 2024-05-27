
# 概要
​
ImageFormatConverterは、PIL を利用した画像変換ツールです。 画像ファイルの形式を簡単に変換することができます。
​
# 機能
​
* png, jpeg, bmpなどのファイルを好きなファイルの形式に変更できる
* ローカルで動作するためユーザーのプライバシーを保護できる

​
## インストール
​
```
pip install pillow
```
​
## 使い方 example
* ライブラリのインポート
```
import pillow as PIL
```
* 処理の設定
* input_file="変換したい画像ファイルのパス"
* output_file="出力したいファイルの名前を入力"
* output_format="出力したい画像の形式"
* →ファイルのパスを'C:/Users/data/melody/image.jpeg'のように設定してください

​
* プログラム例
```
# フォルダパスを設定
input_folder = 'C:/Users/data/image1.jpeg'
output_folder = 'C:/Users/data/image2.png'
output_format = "png"
​
# 変換処理を実行
convert_image_format(input_file, output_file, output_format)
```
​

​
# 変換後の注意
​
* 変換するファイルが存在していることを確認してください。。

​
# サポート
​
バグ報告や機能リクエストは、GitHubまたは、メールにてご連絡ください。
​
# ライセンス
​
このプログラムは [MIT License](https://choosealicense.com/licenses/mit/) でライセンスされています。
​
## バージョン
​
0.1.6