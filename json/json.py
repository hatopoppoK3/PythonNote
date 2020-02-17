import json
import pprint

sample = {}
# jsonをdict形式で読み込み
with open('./json/input.json', 'r', encoding='UTF-8') as f:
    sample = json.load(f)
pprint.pprint(sample)
print('\n{0}:{1} deleted.'.format('_id', sample.pop('_id')))
print('{0}:{1} deleted.'.format('name', sample.pop('name')), end='\n\n')

# dictをjson形式で書き込み
with open('./json/output.json', 'w', encoding='UTF-8') as f:
    json.dump(sample, f, indent=4)
pprint.pprint(sample)

# 文字列をdictに変換
string = '{\"name\":\"poppo\",\"age\":\"20\"}'
sample = json.loads(string)
pprint.pprint(sample)

# dictを文字列に変換
string = ''
string = json.dumps(sample)
pprint.pprint(string)
