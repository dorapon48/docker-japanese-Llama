import sys
from huggingface_hub import snapshot_download
# model_id = "elyza/ELYZA-japanese-Llama-2-7b-fast-instruct"
model_id = sys.argv[1]
file_name = sys.argv[2]
# model_id = "elyza/ELYZA-japanese-Llama-2-7b-instruct"
# file_name = "ELYZA-japanese-Llama-2-7b-instruct"
if (model_id != "" and file_name != ""):
    snapshot_download(repo_id=model_id, local_dir=file_name,
        local_dir_use_symlinks=False, revision="main")
else:
    print("error:wrong argument")
