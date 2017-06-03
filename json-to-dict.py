import json
json_data = json.loads(open('customer.json').read())
python_obj = json_data
r1=python_obj
print(python_obj['address']['streetAddress'])
print(r1)


