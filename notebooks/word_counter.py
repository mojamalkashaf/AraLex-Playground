import json
import re
import os

# Regular expression for Arabic words
arabic_word_regex = re.compile(r'[\u0600-\u06FF]+')

# Function to count Arabic words in a JSON file
def count_arabic_words(json_data):
    if isinstance(json_data, dict):
        json_data = json.dumps(json_data, ensure_ascii=False)
    elif isinstance(json_data, list):
        json_data = ' '.join([json.dumps(item, ensure_ascii=False) for item in json_data])
    
    # Find all Arabic words using regex
    arabic_words = arabic_word_regex.findall(json_data)
    
    return len(arabic_words)

# Function to process all JSON files in a folder and count Arabic words
def count_arabic_words_in_folder(folder_path):
    total_arabic_words = 0

    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            file_path = os.path.join(folder_path, filename)
            
            # Load each JSON file
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Count Arabic words in the file
            arabic_word_count = count_arabic_words(data)
            total_arabic_words += arabic_word_count
            
            print(f'{filename}: {arabic_word_count} Arabic words')
    
    return total_arabic_words

# Folder containing the JSON files
folder_path = 'upload'

# Call the function to count Arabic words in all JSON files in the folder
total_arabic_word_count = count_arabic_words_in_folder(folder_path)
print(f'Total Arabic words found in all files: {total_arabic_word_count}')
