from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema
from rest_framework.views import APIView



from utils.centres import TouristCentre
from utils.cities import City
from utils.states import State

import coreapi
import json


class StateList(APIView):

    schema = AutoSchema(
        manual_fields=[
            coreapi.Field("name",
            required = False,
            location= 'query',
            description = 'Get a particular Nigerian state by its name')

        ]
    )

    def get(self, request):

        
        if request.GET.get('name', False):
            param = request.GET['name'].capitalize()
            obj = State()
            data = obj.getState(param)
        else:
            obj = State()  
            data = obj.getAll()
        if data:
            return Response(data)
        else:
            return Response(data={'details':'No content was found'} , status=status.HTTP_204_NO_CONTENT)

class CityList(APIView):

    schema = AutoSchema(
        manual_fields=[
            coreapi.Field("name",
            required = False,
            location= 'query',
            description = 'Get a particular Nigerian city or town by its name')

        ]
    )


    def get(self, request):
        if request.GET.get('name', False):
            param = request.GET['name'].capitalize()
            obj = City()
            data = obj.getCity(param)
        else:
            obj = City()
            data = obj.getAll()
                     
        
        if data:
            return Response(data)
        else:
           return Response(data={'details':'No content was found'}, status=status.HTTP_204_NO_CONTENT)

class TouristCentreList(APIView):
    schema = AutoSchema(
        manual_fields=[
            coreapi.Field("name",
            required = False,
            location= 'query',
            description = 'Get a particular Nigerian tourist centre by its name(s)'),
            coreapi.Field("town",
            required = False,
            location= 'query',
            description = 'Filter the tourist centres by the name of a Nigerian town'),
            coreapi.Field("state",
            required = False,
            location= 'query',
            description = 'Filter the tourist centres by the name of a Nigerian state'),
        ]
    )


    def get(self, request):

        if request.GET.get('name', False) and request.GET.get('town', False) and request.GET.get('state', False):
            centre = request.GET['name']
            town = request.GET['town']
            state = request.GET['state']   
            obj = TouristCentre()      
            data = obj.getCentre(centre=centre, town=town, state=state)
            

        elif request.GET.get('name', False) and request.GET.get('town', False):
            centre = request.GET['name']
            town = request.GET['town']
            obj = TouristCentre()      
            data = obj.getCentre(centre=centre, town=town)
        

        elif request.GET.get('name', False) and request.GET.get('state', False):
            centre = request.GET['name']
            state = request.GET['state']
            obj = TouristCentre()      
            data = obj.getCentre(centre=centre, state=state)
            
        
        elif request.GET.get('name', False):
            param = request.GET['name']
            obj = TouristCentre()      
            data = obj.getCentre(param)
            
        
        elif request.GET.get('state', False):
            param = request.GET['state'].capitalize()
            obj = TouristCentre()
            data = obj.getCentres(state=param)
            

        elif request.GET.get('town', False):
            param = request.GET['town'].capitalize() 
            obj = TouristCentre()
            data = obj.getCentres(town=param)
        
        else:
            obj = TouristCentre()
            data = obj.getAll()
            
        if data:
            return Response(data)
        else:
            return Response(data={'details':'No content was found'}, status=status.HTTP_204_NO_CONTENT)