from django.shortcuts import render

from farm.models import Farm


def homepage(request):
    farm_list = Farm.objects.all()
    context = {'farm_list': farm_list}
    return render(request, 'homepage/homepage.html', context)
