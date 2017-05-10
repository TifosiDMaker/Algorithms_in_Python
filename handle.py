import os
import csv


dest_dir = 'D:/Tifosi/术语库'
for root, dirs, files in os.walk(dest_dir):
    for name in files:
        if '.csv' in name:
            headers = []
            long_name = os.path.join(root, name)
            with open(long_name, 'r', encoding='utf-8',errors='ignore') as f:
                reader = csv.reader(f)
                for i, header in enumerate(next(reader)):
                    try:
                        if ">>L<<" in header:
                            headers.append(i)
                    except StopIteration:
                        pass
                        GeneratorExit
                print(headers)
            with open(long_name, 'r', encoding='utf-8', errors='ignore') as ff:
                reader2 = csv.reader(ff)
                with open(root + '/' + name[:-5] + '_result.csv', 'w',errors='ignore', newline='') as result:
                    wtr = csv.writer(result)
                    newrow = []
                    for row in reader2:
                        for n in headers:
                            try:
                                newrow.append(row[n])
                            except:
                                print(root)
                        wtr.writerow(newrow)
                        newrow = []
