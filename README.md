# keras-models

Python 3.7.13
## Freeze 

`conda env create -f conda-age-gender.yaml`
`conda env export > conda-age-gender.yaml`


|ディレクトリ|内容|備考|
|---|----|---|
|models/keras|kerasの学習済みモデル||
|cache/|変数のキャッシュを保存する|中身はプッシュしない|
|dataset/file|データの置き場所|中身はプッシュしない|
|njs|NodeJS用のモデルラッパー||

## keras-pythonモデルをJS用に変換

```bash
MODEL=model.h5
JS_MODEL_DIR=vgg16-model
tensorflowjs_converter --input_format keras $MODEL njs/$JS_MODEL_DIR
```


## v2017 Macの場合

```bash
pip3 install plaidml-keras plaidbench
pip3 install keras
export PLAIDML_NATIVE_PATH=/usr/local/lib/libplaidml.dylib
export RUNFILES_DIR=/usr/local/share/plaidml
export KERAS_BACKEND=plaidml.keras.backend

plaidml-setup
python3 mac_intel_keras.py
```