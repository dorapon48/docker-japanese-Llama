#!/usr/bin/env bash

# mkdir
mkdir /data/download
mkdir /data/models

cd /download

source ./.env

# download model
if [ ! -e /data/download/${hf_model_file_name} ];then 
    python3 download.py ${hf_model_id} ${hf_model_file_name}
    # mv ELYZA-model /data/download
    mv ${hf_model_file_name} /data/download
fi

gguf_name=${hf_model_file_name}_${convert_outtype}.gguf

# convert model
cd /data/download
if [ ! -e /data/models/${gguf_name} ];then 
    python3 /opt/llama.cpp/convert.py ${hf_model_file_name}/ --outfile ${gguf_name} --outtype ${convert_outtype}
    mv ${gguf_name} /data/models
fi
