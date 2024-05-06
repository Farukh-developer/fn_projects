from django.shortcuts import render 


from.models import Country
def country(request):
    count=Country.objects.all()
    return render(request, 'country.html', context={"count":count})



def read_one_student(request):
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

# add (Read)

def read_one_comapany(request, id):
    comp=Company.objects.get(id=id)
    return render(request, 'read_location.html', context={"comp":comp})

def read_country(request, id):
    count=Country.objects.get(id=id)
    return render(request, 'read_country.html', context={"count":count})

def read_food(request, id):
    meal=Food.objects.get(id=id)
    return render(request, 'read_food.html', context={"meal":meal} )

def read_latop(request, id):
    computer=Laptop.objects.get(id=id)
    return render(request, 'read_laptop.html', context={"computer":computer}) 


def read_phone(request, id):
    mobile=Phone.objects.get(id=id)
    return render(request, 'read_phone.html', context={"mobile":mobile}) 