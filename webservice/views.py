from random import randint
import json


def read_file(filename) -> str:
    with open(filename) as file:
        return file.read()


def clean_text(text: str) -> list:
    """This function assists when we need count the letters with no blank space."""
    cleaned_text = text.replace(" ", "")
    return cleaned_text


def returns_text_data(text: str) -> dict:
    array_of_text = text.split("\n")
    array_of_text_len = len(array_of_text)
    random_number = randint(1, array_of_text_len-1)
    choosed_line = array_of_text[random_number]
    
    data = {
        "line_text": choosed_line,
        "index_line": array_of_text.index(choosed_line)
    }
    response = json.dumps(data)
    return response
