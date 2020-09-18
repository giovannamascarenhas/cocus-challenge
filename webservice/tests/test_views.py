from django.test import TestCase
import json

from webservice.views import (
    read_file,
    clean_text,
    returns_text_data
)


class TestView(TestCase):
    
    def setUp(self):
        self.filename = "textfile_directory/my_text.txt"
        self.generated_text = read_file(self.filename)
        self.text_data = {
            "line_text": "The entire reading component must be written in English", 
            "index_line": 12 
        }
        
    def test_read_file(self):
        self.assertIsInstance(self.generated_text, str)

    def test_clean_text(self):
        text = "This is a random text for tests purposes."
        cleaned_text = clean_text(text)
        self.assertNotEqual(text, cleaned_text)
        self.assertIsInstance(cleaned_text, str)

    def test_returns_text_data(self):
        data_text = returns_text_data(self.generated_text)
        data_text_to_python_dict = json.loads(data_text)
        self.assertIn("line_text", data_text_to_python_dict.keys())
        self.assertIn("index_line", data_text_to_python_dict.keys())
        self.assertIsInstance(data_text_to_python_dict, dict)
