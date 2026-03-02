from django.urls import path

# esse import busca pelo arquivo 'view.py' no __init__.py da pasta view
from contact import views 
app_name = 'contact'

urlpatterns = [
    path('<int:contact_id>/', views.contact, name='contact'),
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),
]
