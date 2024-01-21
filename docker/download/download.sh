#!/usr/bin/env bash

# ディレクトリ作成
mkdir /data/download
mkdir /data/models

cd /download

source ./.env

if [ ! -e /data/download/ELYZA-model ];then 
    python3 download.py $hf_model_id $hf_model_file_name
    # mv ELYZA-model /data/download
    mv $hf_model_file_name /data/download
fi

# python3 /opt/llama.cpp/convert.py --input ELYZA-model --output ELYZA-model.gguf