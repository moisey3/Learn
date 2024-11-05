# TODO Напишите функцию для поиска индекса товара


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

def poisk(items_list_def, find_item_def):
    i = 0
    for item in items_list:
        i += 1
        if item == find_item:
            return i-1

for find_item in ['банан', 'груша', 'персик']:
    index_item = poisk(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
