from django.shortcuts import render, redirect
from.models import Country


def country(request):
    count=Country.objects.all()
    return render(request, 'country.html', context={"count":count})
    
def read_country(request, id):
    count=Country.objects.get(id=id)
    return render(request, 'read_country.html', context={"count":count})

def create_country(request):
    return render(request, 'create.html')

def save_country(request):
    if request.method=='POST':
        data=request.POST
        country=Country()
        country.capital_city=data['capital_city']
        country.population=data['population']
        country.language=data['language']
        country.save()
        
        return redirect('country')
    return render(request, 'create.html')

def update_country(request,id):
    count=Country.objects.get(id=id)
    if request.method=='POST':
        data=request.POST
        count.capital_city=data['capital_city']
        count.population=data['population']
        count.language=data['language']
        count.save()
        return redirect('country')

    return render(request, 'update_country.html', context={"count":count})

def delete_country(request, id):
    count=Country.objects.get(id=id)
    count.delete()
    return redirect('country')
        
    
    
#2 #############################################

from.models import Company

def company(request):
    comp=Company.objects.all()
    return render(request, 'company.html', context={"comp":comp})

def read_company(request, id):
    comp=Company.objects.get(id=id)
    return render(request, 'read_location.html', context={"comp":comp})


def create_company(request):
    return render(request, 'create_company.html')


def save_company(request):
    if request.method=='POST':
        data=request.POST
        comp=Company()
        comp.company_name=data['company_name']
        comp.location=data['location']
        comp.save()
        
        return redirect('company')
    
    return render(request, 'create_company.html')

def update_company(request, id):
    comp=Company.objects.get(id=id)
    if request.method=='POST':
        data=request.POST
        comp.company_name=data['company_name']
        comp.location=data['location']
        comp.save()
        return redirect('company')
    return render(request, 'update_company.html',context={"comp":comp})


def delete_company(request, id):
    comp=Company.objects.get(id=id)
    comp.delete()
    return redirect('/company')
        
#3 ##########################################################
from.models import Phone

def phone(request):
    mobile=Phone.objects.all()
    return render(request, 'phone.html', context={"mobile":mobile})
def read_phone(request, id):
    mobile=Phone.objects.get(id=id)
    return render(request, 'read_phone.html', context={"mobile":mobile}) 

def create_phone(request):
    return render(request, 'create_phone.html')

def save_phone(request):
    if request.method=='POST':
        data=request.POST
        mobile=Phone()
        mobile.model=data['model']
        mobile.color=data['color']
        mobile.price=data['price']
        mobile.save()
        
        return redirect('/phone')
    
    return render(request, 'create_phone.html')

def update_phone(request, id):
    mobile=Phone.objects.get(id=id)
    if request.method=='POST':
        data=request.POST
        mobile.model=data['model']
        mobile.color=data['color']
        mobile.price=data['price']
        mobile.save()
        return redirect('/phone')
    return render(request, 'update_phone.html',context={"mobile":mobile})
        
        
def delete_phone(request, id):
    mobile=Phone.objects.get(id=id)
    mobile.delete()
    return redirect('/phone')
            


#3 ###############################

from.models import Food

def food(request):
    meal=Food.objects.all()
    return render(request, 'food.html', context={"meal": meal})

def read_food(request, id):
    meal=Food.objects.get(id=id)
    return render(request, 'read_food.html', context={"meal":meal})

def create_food(request):
    return render(request, 'create_food.html')


def save_food(request):
    if request.method=='POST':
        data=request.POST
        meal=Food()
        meal.name=data['name']
        meal.country=data['country']
        meal.save()
        
        return redirect('/food')
    
    return render(request, 'create_food.html')


def update_food(request, id):
    meal=Food.objects.get(id=id)
    if request.method=='POST':
        data=request.POST
        meal.name=data['name']
        meal.country=data['country']
        meal.save()
        return redirect('/food')
    return render(request, 'update_food.html',context={"meal":meal})


def delete_food(request, id):
    meal=Food.objects.get(id=id)
    meal.delete()
    return redirect('/food')
        

from.models import Laptop
 
def laptop(request):
    computer=Laptop.objects.all()
    return render(request, 'laptop.html', context={"computer":computer})

def read_latop(request, id):
    computer=Laptop.objects.get(id=id)
    return render(request, 'read_laptop.html', context={"computer":computer}) 


def create_laptop(request):
    return render(request, 'create_laptop.html')

def save_laptop(request):
    if request.method=='POST':
        data=request.POST
        computer=Laptop()
        computer.model=data['model']
        computer.color=data['color']
        computer.price=data['price']
        computer.save()
    
        return redirect('/laptop')
    
    return render(request, 'create_laptop.html')


        
def update_laptop(request, id):
    computer=Laptop.objects.get(id=id)
    if request.method=='POST':
        data=request.POST
        computer.model=data['model']
        computer.color=data['color']
        computer.price=data['price']
        computer.save()
        return redirect('/laptop')
    return render(request, 'update_laptop.html',context={"computer":computer})
        


        
def delete_laptop(request, id):
    computer=Laptop.objects.get(id=id)
    computer.delete()
    return redirect('/laptop')
                