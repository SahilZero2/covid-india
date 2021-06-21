from django.urls import path
from .views import covidstate


urlpatterns = [
    path('state/<str:state>/', covidstate, name='covidstate'),
]