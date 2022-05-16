
from django.shortcuts import redirect, render
from cars.models import CarTeam

from pages.models import Team
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def home(request):
    teams=Team.objects.all()
    featured_car=CarTeam.objects.order_by('date_created').filter(is_featured=True)
    # search_homeForm=CarTeam.objects.values( 'model','city','year','bode_style','car_name','bode_style') 
    model_search_home=CarTeam.objects.values_list('model', flat=True).distinct()
    year_search_home=CarTeam.objects.values_list('year', flat=True).distinct()
    city_search_home=CarTeam.objects.values_list('city', flat=True).distinct()
    body_search_home=CarTeam.objects.values_list('bode_style', flat=True).distinct()
    
    data={
        'teams':teams,
        'featured_car':featured_car,
        # 'search_homeForm':search_homeForm,
        'model_search_home':model_search_home,
        'year_search_home':year_search_home,
        'city_search_home':city_search_home,
        'body_search_home':body_search_home,
    }

    return render(request,'pages/home.html',data)

def about(request):
    return render(request,'pages/about.html')

def services(request):
    return render(request,'pages/services.html')

def contact(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        phone=request.POST['phone']
        message=request.POST['message']

        # send email to admin 
        if request.user.is_authenticated:
            admin_info = User.objects.get(is_superuser=True)
            admin_email=admin_info.email

            send_mail(
                subject,
                'Name : '+ name +' '+ ' phone : ' + phone +' '+' email : '+ email +' ' +' message : '+  message  ,
                'socialhelp67@gmail.com',
                [admin_email],
                fail_silently=False,
            )
            
            messages.success(request, 'successfully send message')
            return redirect('contact')
        else:
            messages.success(request, 'You should login first')
            return redirect('contact')
        

    return render(request,'pages/contact.html')
