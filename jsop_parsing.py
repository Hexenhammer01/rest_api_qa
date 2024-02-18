import json

string_as_json_format = '{"answer" : "Hello, User"}'
object = json.loads(string_as_json_format)
key = "answer"

if key in object:
    print(object[key])
else:
    print(f"Ключа {key} в json нет")