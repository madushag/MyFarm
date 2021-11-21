from django.shortcuts import render

from produce.models import Produce


def homepage(request):
    produce_list = Produce.objects.all()
    context = {'produce_list': produce_list}
    return render(request, 'produce/customer_view.html', context)

