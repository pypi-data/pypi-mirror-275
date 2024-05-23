import os
import json
import jsonlines
import argparse

def convert_data(input_path):
    raw_data = []
    with open(input_path, 'r', encoding='utf-8') as f:
        s = f.read()
        j = json.loads(s)
        for k, v in j.items():
            raw_data.append({'id': k, 'prompt': v['origin_prompt'], 'prediction': v['prediction']})

    return raw_data