from django.test import TestCase, Client
from django.urls import reverse

from app.views import (
    counting_letters,
    save_text_data_into_database,
    add_another_line,
    list_text_line
)
from webservice.views import (
    read_file,
    clean_text,
    returns_text_data,
)
from app.models import TextModel

class TestView(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.list_text_line_url = reverse("list_text_line")
        self.filename = "textfile_directory/my_text.txt"
        self.generated_text = read_file(self.filename)
        self.text_data = {
            "line_text": "The entire reading component must be written in English", 
            "index_line": 12 
        }
        self.created_text_line = TextModel.objects.create(
            text_line="This is a random text for tests purposes.",
            most_frequency_character="o",
            line_index=6
        )
        
    def test_read_file(self):
        self.assertIsInstance(self.generated_text, str)

    def test_clean_text(self):
        text = "This is a random text for tests purposes."
        cleaned_text = clean_text(text)
        self.assertNotEqual(text, cleaned_text)
        self.assertIsInstance(cleaned_text, str)

    def test_returns_text_data(self):
        data_text = returns_text_data(self.generated_text)
        self.assertIn("line_text", data_text.keys())
        self.assertIn("index_line", data_text.keys())
        self.assertIsInstance(data_text, dict)

    def test_counting_letters(self):
        text = "This is a random text for tests purposes."
        counted_letters = counting_letters(text)
        self.assertIsInstance(counted_letters, dict)

    def test_save_text_into_database_success(self):
        text_data_info = save_text_data_into_database(self.text_data)
        self.assertIsInstance(text_data_info, TextModel)

    def test_save_text_into_database_fail(self):
        text_data = {
            "line_text": "The entire reading component must be written in English", 
            "index_line": 6 
        }
        text_data_info = save_text_data_into_database(text_data)
        self.assertNotIsInstance(text_data_info, TextModel)
        self.assertEquals(text_data_info, {})

    def test_add_another_line(self):
        response = self.client.get(
            reverse("add_another_line"),
            data={
                "line": "Random text line",
                "most_frequency_character": "t",
                "index_line": 1
            },
            content_type='application/json',
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        
        self.assertEquals(response.status_code, 200)
        self.assertTrue(response, "application/json")

    def test_list_text_line_list_GET(self):
        response = self.client.get(self.list_text_line_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "app/index.html")
