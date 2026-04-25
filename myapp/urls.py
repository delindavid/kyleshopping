from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shop/', views.shop, name='shop'),
    path('shop1/', views.shop1, name='shop1'),# ⭐ THIS FIXES NoReverseMatch
    path('payment/', views.payment, name='payment'),
    path('success/', views.success, name='success'),
]