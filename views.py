# Set up the URLs and views for the platform

from django.shortcuts import render
from .models import TonePreset, Comment, Rating

def home(request):
    presets = TonePreset.objects.all()
    return render(request, 'home.html', {'presets': presets})

def preset_detail(request, preset_id):
    preset = TonePreset.objects.get(id=preset_id)
    comments = Comment.objects.filter(preset=preset)
    ratings = Rating.objects.filter(preset=preset)
    return render(request, 'preset_detail.html', {'preset': preset, 'comments': comments, 'ratings': ratings})
