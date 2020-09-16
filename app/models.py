from django.db import models


class TextModel(models.Model):
    text_line = models.CharField(max_length=1000)
    most_frequency_character = models.CharField(max_length=100)
    line_index = models.CharField(max_length=100)

    def __str__(self):
        return self.text_line
