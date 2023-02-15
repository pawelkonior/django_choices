from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('products/create', views.AddProductView.as_view(), name='product_create'),
    path('products/create/custom', views.AddProductCustomFormView.as_view(), name='product_create_custom_form'),

]
