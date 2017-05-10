import os
import csv


dest_dir = 'D:/Tifosi/术语库'
headers = []

for root, dirs, files in os.walk(dest_dir):
    for name in files:
        if 'result' in name:
            long_name = os.path.join(root, name)
            with open(long_name, 'r', encoding='utf-8', errors='ignore') as f:
                reader = csv.reader(f)
                if len(next(reader)) > 2:
                    print(name)