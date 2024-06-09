from django.urls import path
from . import views

urlpatterns = [
  path("",views.home, name='home'),
  path('store/',views.store_page, name='store'),
  path('products/<int:pk>/', views.products, name='products'),
 
]
