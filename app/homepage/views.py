from django.conf import settings
from django.shortcuts import render

from produce.models import Produce, name_choices


def homepage(request):
    produce_filter = request.GET.get('produce')
    distance_filter = request.GET.get('distance')
    lng = request.GET.get('lng')
    lat = request.GET.get('lat')

    if produce_filter and produce_filter != "All":
        # produce_filter = request.GET.get('produce')
        produce_list = Produce.objects.all().filter(name=produce_filter)
        if not produce_list:
            context = {'error_message': f'No {produce_filter} available', 'filter_values': name_choices, 'maps_api_key': settings.GOOGLE_MAPS_API_KEY}
        if distance_filter and distance_filter != "-1":
            for produce in produce_list:
                if produce.get_distance(lat, lng) > int(distance_filter):
                    produce_list = produce_list.exclude(id=produce.id)
    else:
        produce_list = Produce.objects.all()

        if distance_filter and distance_filter != "-1":
            for produce in produce_list:
                produce.distance_from_customer = produce.get_distance(lat, lng)
                if produce.get_distance(lat, lng) > int(distance_filter) or produce.get_distance(lat, lng) == -1:
                    produce_list = produce_list.exclude(id=produce.id)
        else:
            for produce in produce_list:
                produce.distance_from_customer = produce.get_distance(lat, lng)

    context = {'produce_list': produce_list, 'filter_values': name_choices, 'maps_api_key': settings.GOOGLE_MAPS_API_KEY}
    return render(request, 'produce/customer_view.html', context)

