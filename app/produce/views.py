from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import Produce, Farm
from .form import ProduceForm

def index(request, farm_id):
    produce_list = Produce.objects.filter(farm=farm_id).filter(farm__farmer=request.user).order_by('-name')
    farm_name = Farm.objects.get(id=farm_id).name
    produce_list.farm_name = farm_name
    context = {'produce_list': produce_list}
    return render(request, 'produce/index.html', context)

def add(request):
    if request.method == 'POST':
        form = ProduceForm(request.POST)

        if form.is_valid():
            produce = Produce(**form.cleaned_data)
            produce.save()

        return HttpResponseRedirect(reverse('farm:index'))
    else:
        form = ProduceForm(use_required_attribute=True)
        return render(request, 'produce/produce_form.html', {'form': form})


# View action to display a list of produce belonging to a farm for a customer
# def customer(request, farm_id):
#     produce_list = Produce.objects.filter(farm=farm_id).order_by('-name')
#     farm_name = Farm.objects.get(id=farm_id).name
#     produce_list.farm_name = farm_name
#     context = {'produce_list': produce_list}
#     return render(request, 'produce/customer_view.html', context)
