from django.conf import settings
from django.shortcuts import render

from produce.models import Produce, name_choices, mode_of_sale


def get_filtered_produce_list(produce_filter, distance_filter, sale_type_filter, lng, lat):
    # ordering the sequence of filter checks optimizing for the least number of results returned to the client,
    # and then by not having to calculate distance for every produce

    # all 3 filters are set
    if produce_filter and distance_filter and sale_type_filter:
        produce_list = Produce.objects.filter(name=produce_filter).filter(mode_of_sale=sale_type_filter)
        for produce in produce_list:
            if produce.get_distance(lat, lng) > int(distance_filter):
                produce_list = produce_list.exclude(id=produce.id)
        return produce_list

    # only produce and sale type filters are set
    if produce_filter and sale_type_filter:
        produce_list = Produce.objects.filter(name=produce_filter).filter(mode_of_sale=sale_type_filter)
        return produce_list

    # only produce filter is set
    if produce_filter:
        produce_list = Produce.objects.filter(name=produce_filter)
        return produce_list

    # only sale type filter is set
    if sale_type_filter:
        produce_list = Produce.objects.filter(mode_of_sale=sale_type_filter)
        return produce_list

    # only distance filter is set
    if distance_filter:
        produce_list = Produce.objects.all()
        for produce in produce_list:
            if produce.get_distance(lat, lng) > int(distance_filter):
                produce_list = produce_list.exclude(id=produce.id)  # remove produce from list if distance is greater than distance filter
        return produce_list

    # if we get this far then no filters are set
    return Produce.objects.all()


def homepage(request):
    produce_filter = request.GET.get('produce')
    distance_filter = request.GET.get('distance')
    sale_type_filter = request.GET.get('saleType')
    lng = request.GET.get('lng')
    lat = request.GET.get('lat')

    produce_list = get_filtered_produce_list(produce_filter, distance_filter, sale_type_filter, lng, lat)
    for produce in produce_list:
        distance = produce.get_distance(lat, lng)
        produce.distance_from_customer = distance

    # if all three filters are set
    # if produce_filter and distance_filter and sale_type_filter:
    #     produce_list = Produce.objects.filter(name=produce_filter).filter(mode_of_sale=sale_type_filter)
    #     for produce in produce_list:
    #         if produce.get_distance(lat, lng) > int(distance_filter):
    #             produce_list = produce_list.exclude(id=produce.id)
    #
    #     # if distance_filter != "-1":
    #     #     for produce in produce_list:
    #     #         if produce.get_distance(lat, lng) > int(distance_filter):
    #     #             produce_list = produce_list.exclude(id=produce.id)
    #     #
    #     # if distance_filter != "-1":
    #     #     for produce in produce_list:
    #     #         if produce.get_distance(lat, lng) > int(distance_filter):
    #     #             produce_list = produce_list.exclude(id=produce.id)
    #
    # elif distance_filter and distance_filter != "-1":
    #     produce_list = Produce.objects.all()
    #
    #     if distance_filter and distance_filter != "-1":
    #         for produce in produce_list:
    #             produce.distance_from_customer = produce.get_distance(lat, lng)
    #             if produce.get_distance(lat, lng) > int(distance_filter) or produce.get_distance(lat, lng) == -1:
    #                 produce_list = produce_list.exclude(id=produce.id)
    #     else:
    #         for produce in produce_list:
    #             produce.distance_from_customer = produce.get_distance(lat, lng)
    #
    # elif sale_type_filter and sale_type_filter != "Any":
    #     produce_list = Produce.objects.all().filter(mode_of_sale=sale_type_filter)
    #
    # else:
    #     produce_list = Produce.objects.all()

    context = {'produce_list': produce_list, 'filter_values': name_choices, 'mode_filter_values': mode_of_sale, 'maps_api_key': settings.GOOGLE_MAPS_API_KEY}
    return render(request, 'produce/customer_view.html', context)

