from django.shortcuts import render

from produce.models import Produce, name_choices


def homepage(request):
    produce_query = request.GET.get('produce')
    if produce_query and produce_query != "All":
      produce_filter = request.GET.get('produce')
      produce_list = Produce.objects.all().filter(name=produce_filter)
      if not produce_list:
        context =  {'error_message': f'No {produce_filter} available', 'filter_values': name_choices}
        return render(request, 'produce/customer_view.html', context)
    else:  
      produce_list = Produce.objects.all()
    context = {'produce_list': produce_list, 'filter_values': name_choices}
    return render(request, 'produce/customer_view.html', context)

