import json

with open("companies.txt", encoding="utf-8") as companies:
    firms = {firm.split()[0]: float(firm.split()[2]) - float(firm.split()[3]) for firm in companies.readlines()}

list_companies = [firms, {"average_profit": sum(map(lambda s: s if s > 0 else 0, firms.values())) / sum(
    map(lambda s: 1 if s > 0 else 0, firms.values()))}]

with open("companies.json", "w", encoding="utf-8") as json_file:
    json.dump(list_companies, json_file)
