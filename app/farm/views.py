from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Farm


def index(request):
    # return HttpResponse("You're looking at a test farm")
    farm_list = Farm.objects.order_by('-name')[:5]
    context = {'farm_list': farm_list}
    return render(request, 'farm/index.html', context)


def details(request, farm_id):
    farm = get_object_or_404(Farm, pk=farm_id)
    return render(request, 'farm/details.html', {'farm': farm})


def add(request):
    farm = Farm(
        name=request.POST['name'],
        description=request.POST['description'],
        phone_no=request.POST['phone']
    )
    farm.save()
    return HttpResponseRedirect(reverse('farm:index'))


def update(request, farm_id):
    farm = get_object_or_404(Farm, pk=farm_id)

    farm.name = request.POST['name']
    farm.description = request.POST['description']
    farm.phone_no = request.POST['phone']

    farm.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('farm:index'))

