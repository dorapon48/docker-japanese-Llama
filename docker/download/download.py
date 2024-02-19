import sys
from huggingface_hub import snapshot_download, HfApi

model_id = sys.argv[1]
file_name = sys.argv[2]

api = HfApi()
in_safetensor = False
in_bin = False

# リポジトリにあるファイルで，safetensorとbinが混在しているとき，
# binを優先する
file_list = list(api.list_repo_files(repo_id=model_id))

for f_name in file_list:
    if '.safetensors' in f_name:
        in_safetensor = True
        break
for f_name in file_list:
    if '.bin' in f_name:
        in_bin = True
        break

# print(in_safetensor)

if in_safetensor:
    if in_bin:
        if (model_id != "" and file_name != ""):
            snapshot_download(repo_id=model_id, local_dir=file_name,
                local_dir_use_symlinks=False, revision="main",
                ignore_patterns=["*.safetensors","*.safetensors.index.json"])
        else:
            print("error: wrong argument")
    else:
        print("error: safetensor is not supported")
else:
    if (model_id != "" and file_name != ""):
        snapshot_download(repo_id=model_id, local_dir=file_name,
            local_dir_use_symlinks=False, revision="main")
    else:
        print("error:wrong argument")

