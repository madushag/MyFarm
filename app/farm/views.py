from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Farm


# Landing page that display the list of farms that belongs to the currently logged in user
def index(request):
    farm_list = Farm.objects.filter(farmer=request.user.id).order_by('-name')[:5]
    context = {'farm_list': farm_list}
    return render(request, 'farm/index.html', context)


# Handler to display farm details
def details(request, farm_id):
    try:
        # filter by user id to prevent information leakage
        farm = Farm.objects.filter(pk=farm_id).filter(farmer=request.user.id).get()
    except Farm.DoesNotExist:
        return render(request, 'farm/details.html', {'error_message': 'Invalid farm ID'})
    else:
        return render(request, 'farm/details.html', {'farm': farm})


# Handler for adding a new farm
def add(request):
    if request.method == 'POST':
        farm = Farm(
            name=request.POST['name'],
            description=request.POST['description'],
            phone_no=request.POST['phone'],
            farmer=request.user
        )
        farm.save()

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('farm:index'))
    else:
        return render(request, 'farm/details.html')


# Handler for saving details of an existing farm
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


# Handler for deleting a farm
def delete(request, farm_id):
    try:
        farm = Farm.objects.get(pk=farm_id)
    except Farm.DoesNotExist:
        return render(request, 'farm/details.html', {'error_message': 'Invalid farm ID'})
    else:
        farm.delete()
        return HttpResponseRedirect(reverse('farm:index'))
