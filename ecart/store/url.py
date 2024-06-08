from django.urls import path
from . import views

urlpatterns = [
  path("",views.home, name='home'),
  path('products/',views.store_page, name='products')
]
