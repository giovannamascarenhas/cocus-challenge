from django.test import TestCase
import json

from webservice.views import (
    random_line
)


class TestView(TestCase):
    
    def setUp(self):
        self.filename = "textfile_directory/my_text.txt"
        self.generated_text = random_line(self.filename)
        self.text_data = {
            "line_text": "The entire reading component must be written in English", 
        }
    
    def test_returns_text_data(self):
        data_text = random_line(self.filename)
        data_text_to_python_dict = json.loads(data_text)
        self.assertIn("line_text", data_text_to_python_dict.keys())
        self.assertIsInstance(data_text_to_python_dict, dict)
