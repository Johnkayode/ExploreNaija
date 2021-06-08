import ast

from .centres import TouristCentre
from .cities import City


class State:

    def __init__(self):

        data = list()
        with open('src/states.txt','r') as f:
            data = ast.literal_eval(f.read())

        states = list()
        for eachState in data:
            state = dict()
            state['id'] = eachState['state']['id']
            state['name'] = eachState['state']['name']
            state['capital'] = eachState['state']['capital']
            state['LGAs'] = eachState['state']['locals']

            city = City()
            stateName = state['name'].split(' ')[0]
           
            cities = city.getCities(stateName)
            state['cities'] = cities

            tourist_centres = TouristCentre()
            centres = tourist_centres.getCentres(state=stateName)
            state['tourist_centres'] = centres



            states.append(state)


        

        self.states = states

    def getAll(self):

        return self.states 

    def getState(self, state=None):
        states = self.states
        state = state + ' ' + 'State'
        return next(filter(lambda obj: obj.get('name') == state, states), None)
    


