import regex as re
from concurrent.futures import ThreadPoolExecutor
import time

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
    print("Time taken:", elapsed_time, "seconds")

    # Save cleaned text to a new file maintaining original line breaks
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(cleaned_text)


