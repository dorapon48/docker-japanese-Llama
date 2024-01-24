#!/usr/bin/env bash

cd /app
source ./.env

python3 -m llama_cpp.server --model /data/models/${model_name} --n_gpu_layers ${n_gpu_layers}