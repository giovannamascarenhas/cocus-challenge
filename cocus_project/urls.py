from django.contrib import admin
from django.urls import path

from app.views import list_text_line, add_one_line


urlpatterns = [
    path('show/', list_text_line, name="show-data"),
    path('ajax/add/', add_one_line, name='add_one_line'),
    path('admin/', admin.site.urls),
]
