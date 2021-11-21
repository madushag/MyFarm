from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import Produce, Farm
from .form import ProduceForm


@login_required(login_url='/register/login/')
def index(request, farm_id):
    produce_list = Produce.objects.filter(farm=farm_id).filter(farm__farmer=request.user).order_by('-name')
    farm_name = Farm.objects.get(id=farm_id).name
    produce_list.farm_name = farm_name
    context = {'produce_list': produce_list}
    return render(request, 'produce/index.html', context)

@login_required(login_url='/register/login/')
def add(request):
    if request.method == 'POST':
        form = ProduceForm(request.user, request.POST)

        if form.is_valid():
            produce = Produce(**form.cleaned_data)
            produce.save()

        return HttpResponseRedirect(reverse('farm:index'))
    else:
        form = ProduceForm(request.user, use_required_attribute=True)
        return render(request, 'produce/produce_form.html', {'form': form})

@login_required(login_url='/register/login/')
def edit(request, produce_id):
    if request.method == 'GET':
        try:
            produce = Produce.objects.filter(pk=produce_id).get()
        except Farm.DoesNotExist:
            return render(request, 'farm/produce.html', {'error_message': 'Invalid produce ID'})
        else:
            return render(request, 'produce/produce_form.html',
                          {'form': ProduceForm(user=request.user, instance=produce, use_required_attribute=True)})

    if request.method == 'POST':
        try:
            produce = Produce.objects.filter(pk=produce_id).get()
        except Produce.DoesNotExist:
            return render(request, 'farm/details_form.html', {'error_message': 'Invalid ID'})
        else:
            form = ProduceForm(request.user, request.POST, instance=produce)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('farm:index'))
            else:
                return render(request, 'produce/produce_form.html', {'form': form})

def delete(request, produce_id):
    try:
        produce = Produce.objects.filter(pk=produce_id).get()
    except Produce.DoesNotExist:
        return render(request, 'farm/details_form.html', {'error_message': 'Invalid ID'})

    else:
        produce.delete()
        return HttpResponseRedirect(reverse('farm:index'))


# View action to display a list of produce belonging to a farm for a customer
def customer(request, farm_id):
    produce_list = Produce.objects.filter(farm=farm_id).order_by('-name')
    farm_name = Farm.objects.get(id=farm_id).name
    produce_list.farm_name = farm_name
    context = {'produce_list': produce_list}
    return render(request, 'produce/customer_view.html', context)
