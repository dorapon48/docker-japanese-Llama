from huggingface_hub import snapshot_download
model_id="elyza/ELYZA-japanese-Llama-2-7b-fast-instruct"
snapshot_download(repo_id=model_id, local_dir="ELYZA-model",
    local_dir_use_symlinks=False, revision="main")
