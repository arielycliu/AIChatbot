"""
This file contains the code to scrap indeed
"""
import os
import re
import pandas as pd

dialogue_folder = "raw_dialogue"
files = os.listdir(dialogue_folder)

dialogue_pattern = r'([a-zA-Z\s]+):(.+)'

data = {
    'name': [],
    'line': []
}

for chpt in files:
    file_path = os.path.join(dialogue_folder, chpt)
    f = open(file_path, "r", encoding='utf-8')
    while True:
        line = f.readline()
        if not line:
            break

        match = re.findall(dialogue_pattern, line)
        if match:
            name, line = match[0]
            # print(f"{name}: {line}")
            data['name'].append(name.strip())
            data['line'].append(line.strip())


df = pd.DataFrame(data)
print(sum(df['name'] == 'Connor'))
df.to_csv('dialogue.csv', index=False)
