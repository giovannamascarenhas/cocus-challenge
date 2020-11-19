from django.test import TestCase, Client
from django.urls import reverse
import json

from app.views import (
    most_repeated_letter,
    save_text_data_into_database
)
from webservice.views import (
    random_line
)
from app.models import TextModel

class TestView(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.list_text_line_url = reverse("list_text_line")
        self.filename = "textfile_directory/my_text.txt"
        self.text_data = {
            "line_text": "The entire reading component must be written in English", 
        }
        self.created_text_line = TextModel.objects.create(
            text_line="This is a random text for tests purposes.",
            most_frequency_character="o",
        )
        
    # def test_counting_letters(self):
    #     text = "This is a random text for tests purposes."
    #     counted_letters = counting_letters(text)
    #     self.assertIsInstance(counted_letters, dict)

    def test_save_text_into_database_success(self):
        text_data_info = save_text_data_into_database(self.text_data)
        self.assertIsInstance(text_data_info, TextModel)

    def test_add_another_line(self):
        response = self.client.get(
            reverse("add_another_line"),
            data={
                "line": "Random text line",
                "most_frequency_character": "t",
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
