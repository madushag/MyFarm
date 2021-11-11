from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .form import FarmDetailsForm
from .models import Farm


# Landing page that display the list of farms that belongs to the currently logged in user
def index(request):
    farm_list = Farm.objects.filter(farmer=request.user.id).order_by('-name')[:5]
    context = {'farm_list': farm_list}
    return render(request, 'farm/index.html', context)


# Handler for adding a new farm
def add(request):
    if request.method == 'POST':
        form = FarmDetailsForm(request.POST)

        if form.is_valid():
            farm = Farm(**form.cleaned_data, farmer=request.user)
            farm.save()

        # if form.is_valid():
        #     farm = Farm(
        #         name=form.cleaned_data['name'],
        #         description=form.cleaned_data['description'],
        #         phone_no=form.cleaned_data['phone_no'],
        #         farmer=request.user
        #     )
        #     farm.save()

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('farm:index'))
    else:
        form = FarmDetailsForm(use_required_attribute=True)
        return render(request, 'farm/details_form.html', {'form': form})


# Handler for displaying and updating details of an existing farm
def details(request, farm_id):
    # if we are displaying the details
    if request.method == 'GET':
        try:
            # filter by user id to prevent information leakage
            farm = Farm.objects.filter(pk=farm_id).filter(farmer=request.user.id).get()
        except Farm.DoesNotExist:
            return render(request, 'farm/details_form.html', {'error_message': 'Invalid farm ID'})

        else:
            return render(request, 'farm/details_form.html',
                          {'form': FarmDetailsForm(instance=farm, use_required_attribute=True)})

    # if we are doing an update
    if request.method == 'POST':
        try:
            # filtering by user id to prevent information leakage
            farm = Farm.objects.filter(pk=farm_id).filter(farmer=request.user.id).get()

        except Farm.DoesNotExist:
            return render(request, 'farm/details_form.html', {'error_message': 'Invalid farm ID'})

        else:
            form = FarmDetailsForm(request.POST, instance=farm)

            if form.is_valid():
                form.save()

                # Always return an HttpResponseRedirect after successfully dealing
                # with POST data. This prevents data from being posted twice if a
                # user hits the Back button.
                return HttpResponseRedirect(reverse('farm:index'))
            else:
                return render(request, 'farm/details_form.html', {'form': form})


# Handler for deleting a farm
def delete(request, farm_id):
    try:
        # filtering by user id to prevent information leakage
        farm = Farm.objects.filter(pk=farm_id).filter(farmer=request.user.id).get()

    except Farm.DoesNotExist:
        return render(request, 'farm/details_form.html', {'error_message': 'Invalid farm ID'})

    else:
        farm.delete()
        return HttpResponseRedirect(reverse('farm:index'))
