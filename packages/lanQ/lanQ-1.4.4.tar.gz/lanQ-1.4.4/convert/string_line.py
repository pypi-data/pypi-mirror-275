import os
import json
import jsonlines
import argparse

def convert_data(input_path):
    id = 0
    raw_data = []
    with open(input_path, 'r', encoding='utf-8') as f:
        for line in f:
            raw_data.append({'id': id, 'content': line})
            id += 1

    return raw_data
