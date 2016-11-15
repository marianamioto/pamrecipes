from django.shortcuts import render


def home(request):
    recipes = ['Bolo de Chocolate', 'Macarrao com Atum', 'panquecas']
    context = {'recipes': recipes}
    return render(request, 'recipe/home.html', context)
