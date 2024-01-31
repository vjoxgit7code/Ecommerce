from django.urls import path
from . import views

app_name = 'search_app'

urlpatterns = [
    path('', views.search_view, name='search_view'),  # Name it 'search_view'
]
