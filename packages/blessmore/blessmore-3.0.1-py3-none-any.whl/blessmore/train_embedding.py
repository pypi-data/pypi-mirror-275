import regex as re
from concurrent.futures import ThreadPoolExecutor
import time
from gensim.models import FastText
from gensim.utils import simple_preprocess
import os

def clean_text_chunk(chunk):
    # Tokenize Shona text
    shona_tokens = re.findall(r'\b\p{L}+\b', chunk.lower())
    
    # Join tokens into cleaned text
    cleaned_text = ' '.join(shona_tokens)
    
    # Remove non-letter symbols
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', cleaned_text)
    
    return cleaned_text

def clean_text_multithreaded(text):
    # Split text into lines
    lines = text.split('\n')
    
    # Clean each line individually
    with ThreadPoolExecutor() as executor:
        cleaned_lines = list(executor.map(clean_text_chunk, lines))
    
    # Join cleaned lines back together with newline characters
    cleaned_text_with_line_breaks = '\n'.join(cleaned_lines)
    
    return cleaned_text_with_line_breaks

def clean_text_from_file(input_file, output_file):
    # Read text from file
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # Measure the start time
    start_time = time.time()

    # Clean the text
    cleaned_text = clean_text_multithreaded(text)

    # Measure the end time
    end_time = time.time()

    # Calculate the elapsed time
    elapsed_time = end_time - start_time

    # Print the elapsed time
    print("Time taken for cleaning:", elapsed_time, "seconds")

    # Save cleaned text to a new file maintaining original line breaks
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(cleaned_text)

def preprocess_text(text):
    text = text.lower()  # Lowercase
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    return simple_preprocess(text)

def read_corpus(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            yield preprocess_text(line)

def train_fasttext_model(corpus_file_path, vector_size):
    # Clean the corpus file
    cleaned_corpus_file_path = 'cleaned_' + os.path.basename(corpus_file_path)
    clean_text_from_file(corpus_file_path, cleaned_corpus_file_path)

    # Read and preprocess the cleaned corpus
    sentences = list(read_corpus(cleaned_corpus_file_path))
    
    start_time = time.time()
    
    # Train FastText model
    model = FastText(
        sentences, 
        vector_size=vector_size,  # Higher dimension for better performance
        window=7, 
        min_count=5, 
        workers=4, 
        sg=1,  # Skip-gram model
        epochs=100,  # More epochs for thorough training
        bucket=2000000,  # Large bucket size for handling subwords
        min_n=3,  # Minimum length of char n-grams
        max_n=6   # Maximum length of char n-grams
    )
    
    end_time = time.time()
    
    # Calculate the elapsed time
    elapsed_time = end_time - start_time
    print("Time taken for training:", elapsed_time, "seconds")
    
    return model


