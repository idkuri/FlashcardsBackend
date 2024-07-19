import os
import json

def read_json_file(filename):
    file_path = os.path.join(os.path.dirname(__file__), filename)
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data