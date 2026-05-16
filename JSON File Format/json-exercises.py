import json

json_str = '{"food": "Hamburger", "color": "Red"}'
print(type(json_str))
data = json.loads(json_str)
print(data["food"])