goods = []
cur_record = 1

while True:
    name = input("Введите наименование товара: ")
    price = int(input("Введите цену товара: "))
    quantity = int(input("Введите количество товара: "))
    units = input("Введите единицы измерения количества товара: ")
    answer = input("Продолжить ввод? (нет/да): ")
    goods.append((cur_record, {"название": name, "цена": price, "количество": quantity, "ед": units}))
    cur_record += 1
    if answer.lower() == "нет":
        break

print(goods)

keys = goods[0][1].keys()
lists = list(map(lambda x: x.copy(), [[]] * len(keys)))

analytics = dict(zip(keys, lists))

for entry in goods:
    good_items = entry[1].items()
    for name, value in good_items:
        analytics.get(name).append(value)

if len(set(analytics.get("ед"))) == 1:
    analytics.update({"ед": list(set(analytics.get("ед")))})

print(analytics)
