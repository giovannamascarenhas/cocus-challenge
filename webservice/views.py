from random import randint
import json


def random_line(filename: str):
    with open(filename) as file:
        data = file.readlines()
    random_number = randint(0, len(data)-1)
    try:
        text = data[random_number]
        text_data = {"line_text": text}
        response = json.dumps(text_data)
        return response 
    except Exception as e:
        return e
