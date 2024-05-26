# text-compare-tool
### English
## Description
This is a tool for comparing two text files and highlighting the differences between them. It uses the `difflib` library to compute the differences and displays added and removed lines in different colors for easy visualization.

## Features
- Compare two text files line by line
- Highlight added lines in green
- Highlight removed lines in red

## Installation
You can install this tool using `pip`:
```
pip install textfile-compare-tool
```

## Usage
To use this tool, run the following command:
```
compare-textfiles --file1 <path_to_file1> --file2 <path_to_file2>
```

## Command Line Arguments
- `--file1`: Path to the first text file for comparison.
- `--file2`: Path to the second text file for comparison.

## Example
Suppose you have two files, file1.txt and file2.txt. You can compare them like this:
```
compare-textfiles --file1 file1.txt --file2 file2.txt
```

### 日本語
## 説明
これは2つのテキストファイルを比較し、その違いをハイライト表示するツールです。`difflib`ライブラリを使用して差分を計算し、追加された行と削除された行を異なる色で表示して、視覚的に分かりやすくします。

## 特徴
- 2つのテキストファイルを行ごとに比較
- 追加された行を緑色でハイライト
- 削除された行を赤色でハイライト

## インストール
このツールはpipを使用してインストールできます:
```
pip install textfile-compare-tool
```

## 使用方法
このツールを使用するには、以下のコマンドを実行します:
```
compare-textfiles --file1 <file1へのパス> --file2 <file2へのパス>
```

## コマンドライン引数
- `--file1`: 比較する最初のテキストファイルへのパスです。
- `--file2`: 比較する2番目のテキストファイルへのパスです。

## 例
例えば、file1.txtとfile2.txtという2つのファイルがあるとします。それらを次のように比較できます:
```
compare-textfiles --file1 file1.txt --file2 file2.txt
```
