dict = {
    "title": {},
    "status": None,
    "severity": None
}

row = [
    "title value", "status value", "seveerity value"
]

client_detail_csv_values = []
for key in ["title", "severity"]:
    index = list(dict.keys()).index(key)
    client_detail_csv_values.append(row[index])

for item in client_detail_csv_values:
    print(item)


