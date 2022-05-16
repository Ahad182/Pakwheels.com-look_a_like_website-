from webbrowser import get
from django.shortcuts import get_object_or_404, render
from cars.models import CarTeam
from django.core.paginator import EmptyPage ,PageNotAnInteger, Paginator
# Create your views here.
def cars(request):
    cars=CarTeam.objects.order_by('date_created')
    paginator=Paginator(cars ,10)
    page=request.GET.get("page")
    paged_car=paginator.get_page(page)
    model_search_home=CarTeam.objects.values_list('model', flat=True).distinct()
    year_search_home=CarTeam.objects.values_list('year', flat=True).distinct()
    city_search_home=CarTeam.objects.values_list('city', flat=True).distinct()
    body_search_home=CarTeam.objects.values_list('bode_style', flat=True).distinct()
    
    data={
        'cars':paged_car,
        'model_search_home':model_search_home,
        'year_search_home':year_search_home,
        'city_search_home':city_search_home,
        'body_search_home':body_search_home,
    }
    return render(request,'cars/cars.html',data)
    
def car_detail(request,id):
    single_car=get_object_or_404( CarTeam ,pk=id)
    data={
        'single_car':single_car,
    }
    return render(request, 'cars/cars_detail.html',data)

def search(request):
    cars=CarTeam.objects.all()
    model_search_home=CarTeam.objects.values_list('model', flat=True).distinct()
    year_search_home=CarTeam.objects.values_list('year', flat=True).distinct()
    city_search_home=CarTeam.objects.values_list('city', flat=True).distinct()
    body_search_home=CarTeam.objects.values_list('bode_style', flat=True).distinct()
    transmision_home=CarTeam.objects.values_list('transmision', flat=True).distinct()
    if 'keyword' in request.GET:
        keyword=request.GET['keyword']
        if keyword:
            cars=cars.filter(description__icontains=keyword)

    if 'model' in request.GET:
        model=request.GET['model']
        if model:
            cars=cars.filter(model__iexact=model)

    if 'city' in request.GET:
        city=request.GET['city']
        if city:
            cars=cars.filter(city__iexact=city)

    if 'year' in request.GET:
        year=request.GET['year']
        if year:
            cars=cars.filter(year__iexact=year)

    if 'bode_style' in request.GET:
        bode_style=request.GET['bode_style']
        if bode_style:
            cars=cars.filter(bode_style__iexact=bode_style)
    if 'min_price' in request.GET:
        min_price=request.GET['min_price']
        max_price=request.GET['max_price']
        if max_price:
            cars=cars.filter(price__gte=min_price,price__lte=max_price)
    if 'transmision' in request.GET:
        transmision=request.GET['transmision']
        if transmision:
            cars=cars.filter(transmision__iexact=transmision)



    data={
        'cars':cars,
        'model_search_home':model_search_home,
        'year_search_home':year_search_home,
        'city_search_home':city_search_home,
        'body_search_home':body_search_home,
        'transmision_home':transmision_home,
    }
    return render(request, 'cars/search.html',data)