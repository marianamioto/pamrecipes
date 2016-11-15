from django.shortcuts import render
from .models import Recipe

def home(request):
    recipes = Recipe.objects.all()
    context = {'recipes': recipes}
    return render(request, 'recipe/home.html', context)
