from django.urls import path
from .views import company, phone, country,laptop,food,read_country,read_company,read_food,read_latop,read_phone,create_country,save_country, create_company,save_company, create_phone, save_phone, update_country, update_company, delete_country, delete_company, update_phone, delete_phone, create_food, save_food, update_food, delete_food, save_laptop, create_laptop, update_laptop, delete_laptop
urlpatterns = [
    path('company/',company),
    path('phone/',phone),
    path('country/',country, name='country'),
    path('laptop/',laptop),
    path('food/',food),
    path('read_company/<int:id>/',read_company, name="read_company" ),
    path('read_country/<int:id>/',read_country, name="read_country" ),
    path('read_food/<int:id>/',read_food, name="read_food" ),
    path('update_company/<int:id>/',update_company, name="update_company" ),
    path('update_country/<int:id>/',update_country, name="update_country" ),
    path('delete_country/<int:id>/',delete_country, name="delete_country" ),
    path('delete_company/<int:id>/',delete_company, name="delete_company" ),
    path('read_latop/<int:id>/',read_latop, name="read_latop" ),
    path('read_phone/<int:id>/',read_phone, name="read_phone" ),
    path('create_country/',create_country, name='create_country'),
    path('save_country/',save_country, name='save_country'),
    path('create_company/',create_company, name='create_company'),
    path('save_company/',save_company, name='save_company'),
    path('create_phone/',create_phone, name='create_phone'),
    path('save_phone/',save_phone, name='save_phone'),
    path('update_phone/<int:id>/',update_phone, name="update_phone" ),
    path('delete_phone/<int:id>/',delete_phone, name="delete_phone" ),
    path('save_food/',save_food, name='save_food'),
    path('create_food/',create_food, name='create_food'),
    path('update_food/<int:id>/',update_food, name="update_food" ),
    path('delete_food/<int:id>/',delete_food, name="delete_food" ),
    path('create_laptop/', create_laptop, name='create_laptop'),
    path('save_laptop/', save_laptop, name='save_laptop'),
    path('update_laptop/<int:id>/',update_laptop, name="update_laptop" ),
    path('delete_laptop/<int:id>/',delete_laptop, name="delete_laptop" ),
    
    
    
    
    
     
    
    
    

]
    
   
