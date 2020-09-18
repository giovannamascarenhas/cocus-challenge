from django.urls import path
from .views import list_text_line, add_another_line


urlpatterns = [
    path('', list_text_line, name="list_text_line"),
    path('ajax/add/', add_another_line, name='add_another_line'),
]
