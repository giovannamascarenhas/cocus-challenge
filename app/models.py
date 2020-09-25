from django.db import models


class TextModel(models.Model):
    text_line = models.CharField(max_length=1000, unique=True)
    most_frequency_character = models.CharField(max_length=1)
    line_index = models.IntegerField()

    def __str__(self):
        return self.text_line
