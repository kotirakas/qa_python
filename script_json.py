import json
import csv

with open("users.json", 'r') as users_list:
    users = json.load(users_list)

with open('books.csv') as books:
    reader = csv.reader(books)
    for row in reader:
        row_dict = {'title': row[0], 'author': row[1], 'height': row[3]}
    # reader = csv.DictReader(books)
    # lst = list(reader)
    # for t in lst:
    #     dar = (t["Title"],t["Author"],t["Height"])
    #
    # print(dar)
    #print(row_dict)

dict_out = {}
for i in users:
    key_dict = ['name', 'gender', 'address', 'books']
    value_dict = [i['name'], i['gender'], i['address'],[row_dict]]
    for x, y in zip(key_dict, value_dict):
        dict_out[x] = y
        json_dict = json.dumps(dict_out, indent=4)
    print(json_dict)
# print(dict_out)

# with open("res.json", 'a') as write_file:
#     json.dump(dict_out, write_file, indent=4)
