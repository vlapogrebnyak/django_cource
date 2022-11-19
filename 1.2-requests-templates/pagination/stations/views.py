from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

import csv

from django.conf import settings

with open(settings.BUS_STATION_CSV, encoding='utf-8') as file:
    dict_reader = csv.DictReader(file)
    CSV_DATA = [item for item in dict_reader]

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):

    paginator = Paginator(CSV_DATA, 10)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    context = {
         'bus_stations': page.object_list,
         'page': page,
    }
    return render(request, 'stations/index.html', context)
