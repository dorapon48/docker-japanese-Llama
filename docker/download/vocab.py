import sys
from transformers import AutoTokenizer
import json

model_d = sys.argv[1]

download_d = "/data/download/" + model_d + "/"

# config確認
with open(download_d + "config.json", "r") as config_file:
    config = json.load(config_file)

tokenizer = AutoTokenizer.from_pretrained(download_d + "/")
vocab = tokenizer.vocab

# トークンでかさ増し
if config["vocab_size"] > tokenizer.vocab_size:
    # U+2581 U+2581
    META_TOKEN = "▁▁"
    for i in range(config["vocab_size"] - tokenizer.vocab_size):
        token = "{}{}".format(META_TOKEN, i)
        vocab[token] = tokenizer.vocab_size + i

with open(download_d + "vocab.json", "w", encoding="utf-8") as vocab_file:
    json.dump(vocab, vocab_file)
