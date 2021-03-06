# keras-models

Python 3.7.13

## Introduction

```shell
pip install -r requirements.txt
```
### About Directory

|ディレクトリ|内容|備考|
|---|----|---|
|models/keras|kerasの学習済みモデル||
|cache/|変数のキャッシュを保存する|中身はプッシュしない|
|dataset|データの置き場所|中身はプッシュしない|
|dataset/file/wiki_corp|https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/wiki_crop.tar|中身はプッシュしない|
|dataset/file/imdb_crop|https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/imdb_crop.tar|中身はプッシュしない|

---


## Face Gender Age Model

### Demo

```shell
wget -P definition https://raw.githubusercontent.com/avelino/python-opencv-detect/master/haarcascade_eye.xml
wget -P definition https://raw.githubusercontent.com/avelino/python-opencv-detect/master/haarcascade_frontalface_alt.xml
python demo.py gender_age
```
### Train

下記二つをdataset/fileに展開する

https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/wiki_crop.tar
https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/imdb_crop.tar

```shell
wget -P definition https://raw.githubusercontent.com/avelino/python-opencv-detect/master/haarcascade_eye.xml
wget -P definition https://raw.githubusercontent.com/avelino/python-opencv-detect/master/haarcascade_frontalface_alt.xml
python train.py gender_age
```
---

## keras-pythonモデルをJS用に変換

```bash
MODEL=model.h5
JS_MODEL_DIR=vgg16-model
tensorflowjs_converter --input_format keras $MODEL njs/$JS_MODEL_DIR
```

## Freeze

` pip freeze > requirements.txt`
