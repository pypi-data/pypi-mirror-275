# 概要

Imap2Dict_kiyoshirouは、.doc、.docx、.xlsx、.pptxファイルを自動的に.pdf形式に変換することができます。

# 機能

* wordファイルやexcelファイルなどをpdf形式に変換する

# 注意点
* 各種ファイル形式の処理に comtypes モジュールと win32com.client を使用します。これらはWindows上でのみ動作するため、Windows環境でこの スクリプトを実行してください。

## インストール

```
pip install comtypes pywin32
```

### 使い方

上記のスクリプトを `file_converter.py` として保存したら、コマンドラインから次のように実行してOfficeファイルをPDFに変換できます。

```sh
python file_converter.py input.docx output.pdf
```

または、以下のように他の形式にも対応しています。

```sh
python file_converter.py input.doc output.pdf
python file_converter.py input.xlsx output.pdf
python file_converter.py input.pptx output.pdf
```

### 注意点
1. このスクリプトはWindows環境専用です。
2. Microsoft Officeがインストールされている必要があります。
3. 必要なPythonパッケージ (`comtypes` と `pywin32`) を事前にインストールしてください。

このスクリプトを実行すると、指定したOfficeファイルがPDFに変換され、指定した出力パスに保存されます。

# サポート

バグ報告や機能リクエストは、GitHubまたは、メールにてご連絡ください。

# ライセンス

このプログラムは [MIT License](https://choosealicense.com/licenses/mit/) でライセンスされています。

## バージョン

0.1.0