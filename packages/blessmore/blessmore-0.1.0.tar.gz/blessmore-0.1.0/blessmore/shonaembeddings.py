import os
from huggingface_hub import hf_hub_download
import gensim

def download_model_files(repo_id, model_dir, model_files):
    os.makedirs(model_dir, exist_ok=True)
    for file_name in model_files:
        hf_hub_download(repo_id=repo_id, filename=f"{model_dir}/{file_name}", local_dir=model_dir)

def load_fasttext_model(model_filename, repo_id="Blessmore/Fasttext_embeddings"):
    model_dir = "Fast_text_50_dim"
    model_files = [
        "shona_fasttext_50d.model",
        "shona_fasttext_50d.model.wv.vectors_ngrams.npy",
        "shona_fasttext_vectors_50d.kv",
        "shona_fasttext_vectors_50d.kv.vectors_ngrams.npy"
    ]
    download_model_files(repo_id, model_dir, model_files)
    model_path = os.path.join(model_dir, model_filename)
    model = gensim.models.FastText.load(model_path)
    return model
