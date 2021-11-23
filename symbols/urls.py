from django.urls import path
from . import views

app_name = 'symbols'

urlpatterns = [
    path('feeds/<int:symbol_type>/', views.list_by_type, name='list_by_type'),
    path('feeds/', views.list_all, name='list_all'),
]
