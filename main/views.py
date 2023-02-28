from django.shortcuts import render, redirect

def index(request):
    return render(request, 'main/index.html', {'title': 'Главная страница'})


def about(request):
    return render(request, 'main/index-1.html', {'title': 'О нас'})


def cars(request):
    return render(request, 'main/index-2.html', {'title': 'Автомобили'})


def services(request):
    return render(request, 'main/index-3.html', {'title': 'Услуги'})


def contacts(request):
    return render(request, 'main/index-4.html', {'title': 'Контакты'})
