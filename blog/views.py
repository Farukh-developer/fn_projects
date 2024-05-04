from django.shortcuts import render 


from.models import Country

def country(request):
    count=Country.objects.all()
    return render(request, 'country.html', context={"count":count})


from.models import Company

def company(request):
    comp=Company.objects.all()
    return render(request, 'company.html', context={"comp":comp})

from.models import Phone

def phone(request):
    mobile=Phone.objects.all()
    return render(request, 'phone.html', context={"mobile":mobile})


from.models import Food

def food(request):
    meal=Food.objects.all()
    return render(request, 'food.html', context={"meal": meal})



from.models import Laptop

def laptop(request):
    computer=Laptop.objects.all()
    return render(request, 'laptop.html', context={"computer":computer})