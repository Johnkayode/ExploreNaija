from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

from .views import CityList, StateList, TouristCentreList



schema_view = get_swagger_view(title = 'Explore Naija API')
schema_view.cls.schema = None

urlpatterns = [
    
    path('states/', StateList.as_view(), name='states_list'),
    path('cities-towns/', CityList.as_view(), name='cities_list'),
    path('tourist-centres/', TouristCentreList.as_view(), name='tourist_centres_list'),
    path('docs/', schema_view)
]


     

