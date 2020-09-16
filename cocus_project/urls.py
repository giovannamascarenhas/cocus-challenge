from django.contrib import admin
from django.urls import path

from app.views import list_text_line, add_another_line


urlpatterns = [
    path('list/', list_text_line, name="list_text_line"),
    path('ajax/add/', add_another_line, name='add_another_line'),
    path('admin/', admin.site.urls),
]
