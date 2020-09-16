from django.test import SimpleTestCase
from django.urls import reverse, resolve

from app.views import list_text_line


class TestUrls(SimpleTestCase):
    def test_list_text_line_url_resolves(self):
        url = reverse("list_text_line")
        url_resolved = resolve(url)
        self.assertEquals(url_resolved.func, list_text_line)
