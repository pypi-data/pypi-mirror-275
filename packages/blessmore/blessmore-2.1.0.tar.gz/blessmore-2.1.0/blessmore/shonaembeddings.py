import os
from huggingface_hub import hf_hub_download
import gensim

def download_model_files(repo_id, model_dir, model_files):
    os.makedirs(model_dir, exist_ok=True)
    for file_name in model_files:
        hf_hub_download(repo_id=repo_id, filename=f"{model_dir}/{file_name}", local_dir=model_dir)

def load_fasttext_model(dimension, repo_id="Blessmore/Fasttext_embeddings"):
    # Define the available dimensions and corresponding folder names
    available_dimensions = [50, 100, 300, 500]
    if dimension not in available_dimensions:
        raise ValueError(f"Invalid dimension. Choose from {available_dimensions}")

    model_dir = f"Fast_text_{dimension}_dim"
    model_files = [
        f"shona_fasttext_{dimension}d.model",
        f"shona_fasttext_{dimension}d.model.wv.vectors_ngrams.npy",
        f"shona_fasttext_vectors_{dimension}d.kv",
        f"shona_fasttext_vectors_{dimension}d.kv.vectors_ngrams.npy"
    ]

    # Download the necessary model files
    download_model_files(repo_id, model_dir, model_files)
    
    # Load the model
    model_path = os.path.join(model_dir, f"shona_fasttext_{dimension}d.model")
    try:
        model = gensim.models.FastText.load(model_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"Model file not found: {model_path}")
    return model
