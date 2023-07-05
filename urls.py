# Inside music_platform/urls.py

from django.urls import path
from music_app.views import home, preset_detail

urlpatterns = [
    path('', home, name='home'),
    path('preset/<int:preset_id>/', preset_detail, name='preset_detail'),
]
