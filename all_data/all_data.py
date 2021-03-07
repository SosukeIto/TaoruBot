import json

# ./all_data/setting.json����ۑ����Ă���token��prefix��擾���܂��B
with open(r'./all_data/setting.json', encoding='utf-8') as fh:
    json_txt = fh.read()
    json_txt = str(json_txt).replace("'", '"').replace('True', 'true').replace('False', 'false')
    token = json.loads(json_txt)['token']
    prefix = json.loads(json_txt)['prefix']

admin_list = [ 605188331642421272, 728911652270899211, 602680118519005184, 526620171658330112 ]