from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path('feeds/', views.AllSymbolsAPI.as_view(), name='all_feeds'),
    path('feeds/<int:symbol_type>/', views.SymbolsByTypeAPI.as_view(),
         name='feeds_by_type'),
]
