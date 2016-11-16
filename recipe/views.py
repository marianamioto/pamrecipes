from django.shortcuts import render
from .models import Recipe


def home(request):
    recipes = Recipe.objects.all()
    context = {'recipes': recipes}
    return render(request, 'recipe/home.html', context)


def recipe(request, pk):
    # TODO:
    # 1- Query for a recipe using the pk
    # 2- Write a context containing the recipe and the ingredients
    # 3- Write (and render) a template to display the whole recipe

    #  XXX: Erase the lines bellow
    from django.http import HttpResponse
    return HttpResponse(pk)
