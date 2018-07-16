import os
import json
path = r'C:\Users\Mitrandir\Downloads'

result_dict = {}
result_dict['Files'] = {}

for roots, dirs, files in os.walk(path):
    for root in roots:
        pass
    for i in range(len(files)):
        if files[i].split('.')[-1] == 'txt':
            with open(os.path.join(roots, files[i]), 'r') as file:
                text = file.read().strip().split()
                len_chars = sum(len(word) for word in text)
            data = {
                files[i]: {
                    "SIZE": os.path.getsize(os.path.join(roots, files[i])),
                    "FORMAT": files[i].split('.')[-1],
                    "LENGTH": len_chars
                }
            }
            result_dict['Files'].update(data)
        else:
            data = {
                files[i]: {
                    "SIZE": os.path.getsize(os.path.join(roots, files[i])),
                    "FORMAT": files[i].split('.')[-1]
                }
            }
            result_dict['Files'].update(data)

with open('test.json', 'w', encoding='utf8') as j_son_file:
    j_son_file.write(json.dumps(result_dict, ensure_ascii=False, indent=4))
print(root)
