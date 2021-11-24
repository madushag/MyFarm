from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.shortcuts import render, redirect
from .models import Produce, Farm
from .form import ProduceForm


@login_required(login_url='/register/login/')
def list_produce(request, farm_id):
    farm = Farm.objects.get(id=farm_id)
    produce_list = Produce.objects.filter(farm=farm_id).filter(farm__farmer=request.user).order_by('-name')
    produce_list.farm_name = farm.name
    produce_list.farm_id = farm_id
    produce_list.farm_website = farm.website_url
    context = {'produce_list': produce_list}
    return render(request, 'produce/index.html', context)


@login_required(login_url='/register/login/')
def add(request, farm_id):
    if request.method == 'POST':
        form = ProduceForm(request.POST, request.FILES)

        if form.is_valid():
            produce = Produce(**form.cleaned_data)
            produce.save()
            return HttpResponseRedirect(reverse('produce:list', args=(farm_id,)))

        else:
            farm_name = Farm.objects.get(id=farm_id).name
            return render(request, 'produce/produce_form.html', {'form': form, 'farm_name': farm_name, 'farm_id': farm_id})
    else:
        form = ProduceForm(use_required_attribute=True)
        farm_name = Farm.objects.get(id=farm_id).name
        return render(request, 'produce/produce_form.html', {'form': form, 'farm_name': farm_name, 'farm_id': farm_id})


@login_required(login_url='/register/login/')
def edit(request, produce_id):
    if request.method == 'GET':
        try:
            produce = Produce.objects.filter(pk=produce_id).get()
        except Farm.DoesNotExist:
            return render(request, 'farm/produce.html', {'error_message': 'Invalid produce ID'})
        else:
            farm_name = produce.farm.name
            farm_id = produce.farm.id
            return render(request, 'produce/produce_form.html', {'form': ProduceForm(instance=produce, use_required_attribute=True),
                                                                 'farm_name': farm_name, 'farm_id': farm_id})

    if request.method == 'POST':
        try:
            produce = Produce.objects.filter(pk=produce_id).get()
        except Produce.DoesNotExist:
            return render(request, 'farm/details_form.html', {'error_message': 'Invalid ID'})
        else:
            form = ProduceForm(request.POST, request.FILES, instance=produce)
            if form.is_valid():
                form.save()
                farm_id = produce.farm.id
                return HttpResponseRedirect(reverse('produce:list', args=(farm_id,)))
            else:
                farm_name = produce.farm.name
                farm_id = produce.farm.id
                return render(request, 'produce/produce_form.html', {'form': form, 'farm_name': farm_name, 'farm_id': farm_id})


def delete(request, produce_id):
    try:
        produce = Produce.objects.filter(pk=produce_id).get()
        farm_id = produce.farm.id
    except Produce.DoesNotExist:
        return render(request, 'farm/details_form.html', {'error_message': 'Invalid ID'})

    else:
        produce.delete()
        return HttpResponseRedirect(reverse('produce:list', args=(farm_id,)))


# View action to display a list of produce belonging to a farm for a customer
def customer(request, farm_id):
    produce_list = Produce.objects.filter(farm=farm_id).order_by('-name')
    farm_name = Farm.objects.get(id=farm_id).name
    produce_list.farm_name = farm_name
    context = {'produce_list': produce_list}
    return render(request, 'produce/customer_view.html', context)
