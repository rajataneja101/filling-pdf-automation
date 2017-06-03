import json



json_data = json.loads(open('customer.json').read())
python_obj = json_data
r1=list(python_obj.values())

print(python_obj)
print(r1)





