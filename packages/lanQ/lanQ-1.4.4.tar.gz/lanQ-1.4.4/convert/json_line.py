import os
import json
import jsonlines
import argparse

def convert_data(input_path):
    raw_data = []
    with open(input_path, 'r', encoding='utf-8') as f:
        for line in f:
            j = json.loads(line)
            raw_data.append({'id': j['id'], 'content': j['content']})

    return raw_data