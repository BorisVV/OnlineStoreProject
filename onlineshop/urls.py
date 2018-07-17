
from django.urls import path, include
from . import views 
app_name = 'onlineshop'
urlpatterns = [
    
    path('', views.display_products, name="product_list"),
    path('<slug:category_slug>/', views.display_products, name="product_category"),
]