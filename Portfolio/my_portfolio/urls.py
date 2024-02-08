from django.urls import path
from .views import home, about
urlpatterns = [
    path('', home, name="my_portfolio-home"),
    path('about/', about, name="my_portfolio-about"),
    
]