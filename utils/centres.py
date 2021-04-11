import json

class TouristCentre:
    def __init__(self):
        self.f = open('src/centres.json', encoding='utf-8')
        
        data = json.load(self.f)

        self.centres = data

    def getAll(self):
        return self.centres

    def getCentre(self, centre=None, town=None, state=None):
        centres = self.centres

        if centre and town is None and state is None:
            return next(filter(lambda obj: centre.lower() in obj.get('name').lower(), centres), None)

        elif centre and town and state is None:
            return next(filter(lambda obj: centre.lower() in obj.get('name').lower() \
                and town.lower() in obj.get('town/city').lower()
            , centres), None)
        elif centre and state and town is None:
            return next(filter(lambda obj: centre.lower() in obj.get('name').lower() \
                and state.lower() in obj.get('state').lower()
            , centres), None)
        else:
            return next(filter(lambda obj: centre.lower() in obj.get('name').lower() \
                and town.lower() in obj.get('town/city').lower() \
                and state.lower() in obj.get('state').lower()
            , centres), None)

    
    def getCentres(self, state=None, town=None):
        '''
        returns all cities in a given stae
        '''

        centres = self.centres 
        if state:
            return [centre for centre in centres if centre['state'] == state]
        elif town:
            return [centre for centre in centres if centre['town/city'] == town]
        return None

