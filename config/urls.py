"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog.views import  company, phone, laptop, food, read_one_comapany, read_country, country, read_food, read_latop, read_phone

urlpatterns = [
    path('admin/', admin.site.urls),
    path('company/',company),
    path('phone/',phone),
    path('country/',country),
    path('laptop/',laptop),
    path('food/',food),
    path('read_one_company/<int:id>/',read_one_comapany, name="read_one_company" ),
    path('read_country/<int:id>/',read_country, name="read_country" ),
    path('read_food/<int:id>/',read_food, name="read_food" ),
    path('read_latop/<int:id>/',read_latop, name="read_latop" ),
    path('read_phone/<int:id>/',read_phone, name="read_phone" )
    
    

    
    
    
    
    
    
    
]
