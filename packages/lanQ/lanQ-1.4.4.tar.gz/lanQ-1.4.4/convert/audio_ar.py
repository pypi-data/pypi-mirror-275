import os
import json
import jsonlines
import argparse

def convert_data(input_path):
    raw_data = []
    with open(input_path, 'r', encoding='utf-8') as f:
        s = f.read()
        j = json.loads(s)
        raw_data.append({'id': j['id'], 'content': j['text']['content']})

    return raw_data