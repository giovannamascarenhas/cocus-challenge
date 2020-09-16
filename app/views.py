from django.shortcuts import render
from django.http import HttpResponse, Http404
import glob
from random import randint
from collections import Counter
import json

from .models import TextModel


# Find a file with .txt extension
FILENAME = "my_text.txt"


def read_file(filename) -> str:
    with open(filename) as file:
        return file.read()


def clean_text(text: str) -> list:
    """This function assists when we need count the letters with no blank space."""
    cleaned_text = text.replace(" ", "")
    return cleaned_text


def returns_text_data(text: str) -> dict:
    # import pdb; pdb.set_trace()
    array_of_text = text.split("\n")
    array_of_text_len = len(array_of_text)
    random_number = randint(1, array_of_text_len-1)
    choosed_line = array_of_text[random_number]
    
    return {
        "line_text": choosed_line,
        "index_line": array_of_text.index(choosed_line)
    }


def counting_letters(line_text: str) -> dict:
    line_text_without_blanck_space = clean_text(line_text)
    number_of_letters_per_line = Counter(line_text_without_blanck_space)
    return number_of_letters_per_line


def save_text_data_into_database(data: dict) -> dict:
    text_line = data["line_text"]
    text_index = data["index_line"]

    letters_counter = counting_letters(text_line)

    most_repeated_letter = max(letters_counter, key=lambda key: letters_counter[key])

    new_text_line = TextModel(text_line=text_line, most_frequency_character=most_repeated_letter, line_index=text_index)

    # Checks if text index exists into database
    if TextModel.objects.filter(line_index=text_index):
        return {}
    else:
        new_text_line.save()
        return new_text_line 


def add_another_line(request):
    if request.is_ajax():
        text = read_file(FILENAME)
        text_data_dict_info = returns_text_data(text)
        data_text = save_text_data_into_database(text_data_dict_info)
        if data_text:
            data = {
                "line": data_text.text_line,
                "most_frequency_character": data_text.most_frequency_character,
                "index_line": data_text.line_index
            }
            response = json.dumps(data)
            return HttpResponse(response, content_type='application/json')
        else:
            message = "Data is empty"
            return HttpResponse(message, content_type='application/json')
    else:
        raise Http404()


def list_text_line(request):
    template_name = "app/index.html"
    list_text_line = TextModel.objects.all()
    return render(request, template_name, {"list_text_line": list_text_line})
