import json
x='{"name":"jhone" , "age":20}'
y=json.loads(x)
print(y["age"])
y=json.dumps(x)
print(y)