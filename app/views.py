from django.shortcuts import render
from django.http import HttpResponse, Http404
import glob
import json

from .models import TextModel
from webservice.views import (
    random_line
)


# Find a file with .txt extension
for filename in glob.glob('textfile_directory/*'):
    FILENAME = filename


def most_repeated_letter(line_text: str) -> str:
    """This function returns the most frequency letter"""
    letters = {}
    for letter in line_text:
        if letter == ' ':
            letters[letter] = 0
        elif letter not in letters:
            letters[letter] = 1
        else:
            letters[letter] += 1
    return max(letters, key=letters.get)


def save_text_data_into_database(data: dict) -> TextModel:
    text_line = data["line_text"]
    letters_counter = most_repeated_letter(text_line)
    new_text_line = TextModel(text_line=text_line, most_frequency_character=letters_counter)
    new_text_line.save()
    return new_text_line 
    

def add_another_line(request):
    if request.is_ajax():
        text = random_line(FILENAME)
        text_data_dict_info = json.loads(text)
        data_text = save_text_data_into_database(text_data_dict_info)
        if data_text:
            data = {
                "line": data_text.text_line,
                "most_frequency_character": data_text.most_frequency_character,
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
