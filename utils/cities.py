import json

class City:
    '''
    Python Class to get cities in Nigeria
    ''' 

    def __init__(self):
        '''
        Initializes the class and converts json to python dictionary
        '''
        self.f = open('src/ng.json')
        
        data = json.load(self.f)
        cities = []
        
        for eachCity in data:
            city = {}
            city['name'] = eachCity['city']
            city['latitude'] = eachCity['lat']
            city['longitude'] = eachCity['lng'] 
            city['state'] = eachCity['admin_name']
            city['country'] = eachCity['country']
            city['country code'] = eachCity['iso2']
        
            cities.append(city)

        self.cities = cities
        

    def getAll(self):
        '''
        returns all cities 
        '''
        return self.cities

    def getCity(self, city=None):
        '''
        returns a particular city
        '''

        cities = self.cities
        return next(filter(lambda obj: obj.get('name') == city, cities), None)

    def getCities(self, state=None):
        '''
        returns all cities in a given stae
        '''

        cities = self.cities  
        
        return [city for city in cities if city['state'] == state]

     

