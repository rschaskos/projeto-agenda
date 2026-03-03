from django.urls import path

# esse import busca pelo arquivo 'view.py' no __init__.py da pasta view
from contact import views

app_name = 'contact'

urlpatterns = [
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),

    # contact (CRUD)
    path('contact/<int:contact_id>/', views.contact, name='contact'),
    path('contact/create/', views.create, name='create'),

]
