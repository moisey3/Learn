# TODO решите задачу
import json

def task() -> float:
    with open('input.json', 'r') as file:
        data = json.load(file)

    sum_ = sum([i['score'] * i['weight'] for i in data])
    return round(sum_, 3)

print(task())