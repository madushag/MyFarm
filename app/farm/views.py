from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .form import FarmDetailsForm
from .models import Farm


# Landing page that display the list of farms that belongs to the currently logged in user
@login_required(login_url='/register/login/')
def index(request):
    farm_list = Farm.objects.filter(farmer=request.user.id).order_by('name')
    context = {'farm_list': farm_list}
    return render(request, 'farm/index.html', context)


# Handler for adding a new farm
@login_required(login_url='/register/login/')
def add(request):
    if request.method == 'POST':
        form = FarmDetailsForm(request.POST)

        if form.is_valid():
            farm = Farm(**form.cleaned_data, farmer=request.user)
            farm.save()
        else:
            return render(request, 'farm/details.html', {'form': form, 'maps_api_key': settings.GOOGLE_MAPS_API_KEY})

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('farm:index'))
    else:
        form = FarmDetailsForm(use_required_attribute=True)
        return render(request, 'farm/details.html', {'form': form, 'maps_api_key': settings.GOOGLE_MAPS_API_KEY})


# Handler for displaying and updating details of an existing farm
@login_required(login_url='/register/login/')
def details(request, farm_id):
    # if we are displaying the details
    if request.method == 'GET':
        try:
            # filter by user id to prevent information leakage
            farm = Farm.objects.filter(pk=farm_id).get()
            if farm.farmer != request.user:
                return render(request, 'farm/details.html', {'error_message': 'You do not have permission to view this farm.'})
        except Farm.DoesNotExist:
            return render(request, 'farm/details.html', {'error_message': 'Invalid farm ID'})

        else:
            return render(request, 'farm/details.html', {'form': FarmDetailsForm(instance=farm, use_required_attribute=True), 'maps_api_key': settings.GOOGLE_MAPS_API_KEY})

    # if we are doing an update
    if request.method == 'POST':
        try:
            # filtering by user id to prevent information leakage
            farm = Farm.objects.filter(pk=farm_id).get()
            if farm.farmer != request.user:
                return render(request, 'farm/details.html', {'error_message': 'You do not have permission to update this farm.'})

        except Farm.DoesNotExist:
            return render(request, 'farm/details.html', {'error_message': 'Invalid farm ID'})

        else:
            form = FarmDetailsForm(request.POST, instance=farm)

            if form.is_valid():
                form.save()

                # Always return an HttpResponseRedirect after successfully dealing
                # with POST data. This prevents data from being posted twice if a
                # user hits the Back button.
                return HttpResponseRedirect(reverse('farm:index'))
            else:
                return render(request, 'farm/details.html', {'form': form, 'maps_api_key': settings.GOOGLE_MAPS_API_KEY})


# Handler for deleting a farm
@login_required(login_url='/register/login/')
def delete(request, farm_id):
    try:
        # filtering by user id to prevent information leakage
        farm = Farm.objects.filter(pk=farm_id).get()
        if farm.farmer != request.user:
            return render(request, 'farm/details.html', {'error_message': 'You do not have permission to delete this farm.'})

    except Farm.DoesNotExist:
        return render(request, 'farm/details.html', {'error_message': 'Invalid farm ID'})

    else:
        farm.delete()
        return HttpResponseRedirect(reverse('farm:index'))
