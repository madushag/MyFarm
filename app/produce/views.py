from django.shortcuts import render
from .models import Produce


def index(request, farm_id):
    produce_list = Produce.objects.filter(farm=farm_id).filter(farm__farmer=request.user).order_by('-name')
    context = {'produce_list': produce_list}
    return render(request, 'produce/index.html', context)




