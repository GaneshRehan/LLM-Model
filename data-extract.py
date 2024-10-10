import os
from tqdm import tqdm

def txt_files_in_dir(directory):
    return [filename for filename in os.listdir(directory) 
            if filename.endswith(".txt") and os.path.isfile(os.path.join(directory, filename))]

folder_path = "P:\\context_aware_chatbot"
input_file = "wizard_of_oz.txt"
output_file_train = "output_train.txt"
output_file_val = "output_val.txt"
vocab_file = "vocab.txt"

file_path = os.path.join(folder_path, input_file)

# Read the entire file
with open(file_path, 'r', encoding='utf-8') as infile:
    text = infile.read()

# Calculate split point (90% for training, 10% for validation)
split_index = int(len(text) * 0.9)

# Write training data
with open(output_file_train, 'w', encoding='utf-8') as outfile:
    outfile.write(text[:split_index])

# Write validation data
with open(output_file_val, 'w', encoding='utf-8') as outfile:
    outfile.write(text[split_index:])

# Create vocabulary
vocab = set(text)

# Write vocabulary file
with open(vocab_file, 'w', encoding='utf-8') as vfile:
    for char in vocab:
        vfile.write(char + '\n')

print("Processing complete.")