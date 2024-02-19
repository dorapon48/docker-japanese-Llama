#!/usr/bin/env bash

# mkdir
if [ ! -e /data/download ];then
    mkdir /data/download
fi
if [ ! -e /data/models ];then
    mkdir /data/models
fi

cd /download

source ./.env

# separate
hf_model_file_name=${hf_model_id#*/}

# download model
if [ ! -e /data/download/${hf_model_file_name} ];then 
    python3 download.py ${hf_model_id} ${hf_model_file_name}
    mv ${hf_model_file_name} /data/download
else
    echo "[log] directory already exists: /data/download/${hf_model_file_name}"
fi

gguf_name=${hf_model_file_name}_${convert_outtype}.gguf

# convert model
cd /data/download
if [ ! -e /data/models/${gguf_name} ];then 
    python3 /opt/llama.cpp/convert.py ${hf_model_file_name}/ --outfile ${gguf_name} --outtype ${convert_outtype}
    mv ${gguf_name} /data/models
else
    echo "[log] file already exists: /data/models/${gguf_name}"
fi
