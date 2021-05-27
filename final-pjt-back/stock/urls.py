from django.urls import path
from . import views

app_name = 'stock'

urlpatterns = [
    path('<str:companyname>/', views.stock, name="stock"),
]
