
from django.shortcuts import redirect, render

from contacts.models import contacts
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User

# Create your views here.
def inquiry(request):
    if request.method == 'POST':
        user_id=request.POST['user_id']
        car_id=request.POST['car_id']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        customer_need=request.POST['customer_need']
        car_title=request.POST['car_title']
        city=request.POST['city']
        state=request.POST['state']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']

        if request.user.is_authenticated:
            user_id=request.user.id
            has_connet=contacts.objects.all().filter(user_id=user_id , car_id=car_id)
            if has_connet:
                messages.error(request,'already submitted')
                return redirect('/cars/'+car_id)

        contact=contacts(user_id=user_id ,car_id=car_id,firstname=firstname,lastname=lastname,customer_need=customer_need,
        car_title=car_title,city=city,state=state,email=email,phone=phone,message=message)

        # email section 

        admin_info = User.objects.get(is_superuser=True)
        admin_email=admin_info.email

        send_mail(
            'New inquiry',
            'you have inquiry of ' + car_title + 'please solve it ',
            'socialhelp67@gmail.com',
            [admin_email],
            fail_silently=False,
        )

        # email end 

        contact.save()
        messages.success(request,'your inquiry successfully submitted')
        return redirect('/cars/'+car_id)