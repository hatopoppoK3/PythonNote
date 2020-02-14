import requests

url = 'https://qiita.com/'
# GET実行
response = requests.get(url)

# HTMLをtextで取得
text = response.text
print(type(text))
# status code取得
status_code = response.status_code
print(type(status_code))
# エンコード取得
encoding = response.encoding
print(type(encoding))
# cookies取得
cookies = response.cookies
print(type(cookies))
# header取得
header = response.headers
print(type(header))

url = 'https://github-contributions-api.now.sh/v1/hatopoppoK3'
response = requests.get(url)
header = response.headers
# content-type取得
content_type = header['content-type'].split(';')[0]
if content_type == 'application/json':
    # jsonを読み込みdict取得
    response_json = response.json()
    print(type(response_json))
