import os
import json
import jsonlines
import argparse

def convert_data(input_path):
    id = 0
    raw_data = []
    with open(input_path, 'r', encoding='utf-8') as f:
        j_l = json.load(f)
        for j in j_l:
            raw_data.append({'id': id, 'content': j['output']})
            id += 1

    return raw_data
